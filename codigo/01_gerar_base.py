#!/usr/bin/env python3
"""
01_gerar_base.py — Gera a BASE SINTÉTICA do razão auxiliar da conta INVESTIMENTOS (Vale S.A.)
da Bradespar S.A. em 31/12/2025.  *** TODOS OS REGISTROS SÃO SINTÉTICOS (FICTÍCIOS) ***

Matrícula: 211014396   |   Semente: 211014396   |   Python 3 + numpy + pandas

O que é sintético e o que é público
-----------------------------------
PÚBLICO  : os TOTAIS (saldo inicial, equivalência, reflexos, JCP, dividendos, saldo final, nº de ações)
           — extraídos das demonstrações financeiras de 31/12/2025 (ver parametros.py).
SINTÉTICO: a divisão desses totais em N registros individuais ("sublotes de custódia"), com datas,
           custodiantes, usuários, horários e os erros inseridos. A Bradespar contabiliza, na realidade,
           uma única linha de investimento; a fragmentação é uma hipótese didática (ver docs/).

Saídas (pasta base_simulada/ e saidas/):
  base_investimento_vale_sintetica.csv(.gz)  — 520.000 registros
  registro_erros_inseridos.csv               — gabarito (NÃO é lido pelos testes de detecção)
  dicionario_variaveis.csv                   — dicionário
  hashes.txt                                 — SHA-256 dos arquivos gerados

Uso:  python3 codigo/01_gerar_base.py
"""
import os, sys, hashlib, gzip, shutil
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(__file__))
import parametros as P

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(RAIZ, "base_simulada")
os.makedirs(OUT, exist_ok=True)

rng = np.random.default_rng(P.SEED)
N_LIMPOS = 519_700            # registros "corretos"
N_DUPL = 300                  # duplicidades inseridas (erro E3) -> total 520.000
N_TOTAL = N_LIMPOS + N_DUPL
Q = P.QTD_ACOES

# ------------------------------------------------------------------ 1. quantidades (inteiros que somam Q)
w = rng.lognormal(mean=0.0, sigma=1.0, size=N_LIMPOS)
q = np.floor(w / w.sum() * (Q - N_LIMPOS)).astype(np.int64) + 1
falta = Q - q.sum()
idx = rng.choice(N_LIMPOS, size=int(falta), replace=True) if falta > 0 else []
for i in idx:
    q[i] += 1
assert q.sum() == Q and q.min() >= 1


# ------------------------------------------------------------------ 2. alocação em centavos (maior resto)
def aloca(total_reais: int) -> np.ndarray:
    """Aloca total (R$) proporcionalmente à quantidade, em centavos, somando EXATAMENTE o total."""
    C = int(total_reais) * 100
    base = (C * q) // Q
    resto = (C * q) % Q
    faltam = C - int(base.sum())
    if faltam:
        ordem = np.argsort(-resto, kind="stable")[:faltam]
        base[ordem] += 1
    assert base.sum() == C
    return base


c_ini = aloca(P.SALDO_INICIAL)
c_eq = aloca(P.EQUIVALENCIA)
c_oci = aloca(P.OCI_REFLEXO)
c_jcp = aloca(P.JCP_BRUTO)
c_div = aloca(P.DIVIDENDOS)
c_fin = c_ini + c_eq + c_oci + c_jcp + c_div
assert c_fin.sum() == P.SALDO_FINAL * 100

# ------------------------------------------------------------------ 3. atributos descritivos sintéticos
dias_orig = rng.integers(0, (pd.Timestamp("2024-12-31") - pd.Timestamp("2017-08-01")).days + 1, N_LIMPOS)
data_origem = pd.Timestamp("2017-08-01") + pd.to_timedelta(dias_orig, unit="D")
custod = rng.choice(["C01", "C02", "C03", "C04", "C05", "C06"], size=N_LIMPOS, p=[.34, .26, .18, .12, .06, .04])

# lançamento da equivalência: 97% automático (SISTEMA) em 31/12/2025 ou até 10/01/2026, 3% manual
manual = rng.random(N_LIMPOS) < 0.03
auto_days = rng.choice([0, 0, 0, 0, 2, 3, 5, 6, 7], size=N_LIMPOS)       # dias após 31/12/2025
dt_lanc = pd.Timestamp("2025-12-31") + pd.to_timedelta(auto_days, unit="D")
hora_auto = rng.integers(19, 24, N_LIMPOS)  # 19h-23h (job noturno)
min_ = rng.integers(0, 60, N_LIMPOS)
sec_ = rng.integers(0, 60, N_LIMPOS)
usuario = np.where(manual, rng.choice([f"U{i:02d}" for i in range(1, 9)], size=N_LIMPOS), "SISTEMA")
# lançamentos manuais: dias úteis 02/01-20/01/2026, 08h-18h
dm = pd.bdate_range("2026-01-02", "2026-01-20")
dt_man = rng.choice(dm.values, size=N_LIMPOS)
dt_lanc = pd.to_datetime(np.where(manual, dt_man, dt_lanc.values))
hora = np.where(manual, rng.integers(8, 19, N_LIMPOS), hora_auto)
tipo_lanc = np.where(manual, "MANUAL", "AUTOMATICO")
conta = np.full(N_LIMPOS, "1.2.1.01", dtype=object)
qty_ext = q.copy()
# o dia útil-padrão do lançamento automático pode cair em fim de semana (rotina batch) -> aceitável (SISTEMA)

df = pd.DataFrame(dict(
    id_lote=[f"LT{i:07d}" for i in range(1, N_LIMPOS + 1)],
    custodiante=custod, data_origem=data_origem.strftime("%Y-%m-%d"),
    quantidade_acoes=q, quantidade_custodia_externa=qty_ext,
    c_ini=c_ini, c_eq=c_eq, c_oci=c_oci, c_jcp=c_jcp, c_div=c_div, c_fin=c_fin,
    data_lancamento=dt_lanc.strftime("%Y-%m-%d"), hora_lancamento=hora, minuto=min_, segundo=sec_,
    usuario_lancamento=usuario, tipo_lancamento=tipo_lanc, conta_contabil=conta,
))
correto_fin = df["c_fin"].copy()          # saldo final "correto" por lote (para o gabarito)

# ------------------------------------------------------------------ 4. inserção de erros (gabarito)
reg = []     # lista de dicts
perm = rng.permutation(N_LIMPOS)
pos = 0


def pega(n):
    global pos
    r = perm[pos:pos + n]
    pos += n
    return r


def log(i, tipo, natureza, campo, orig, novo, efeito_cents, desc):
    reg.append(dict(indice=int(i), tipo_erro=tipo, natureza=natureza, campo=campo,
                    valor_original=orig, valor_inserido=novo, efeito_saldo_brl=round(efeito_cents / 100, 2),
                    descricao=desc))


# E1a: equivalência com taxa errada (componente alterado, saldo recalculado de forma consistente)
for i in pega(400):
    f = rng.choice([1.25, 1.36, 0.80, 2.0])
    old = int(df.at[i, "c_eq"]); new = int(round(old * f))
    df.at[i, "c_eq"] = new; df.at[i, "c_fin"] += new - old
    log(i, "E1a", "valor", "equivalencia_2025_brl", old / 100, new / 100, new - old,
        f"equivalência calculada com fator {f} (taxa/participação indevida); saldo recalculado")
# E1b: erro de soma (saldo_final não confere com as parcelas)
for i in pega(300):
    delta = int(rng.choice([-1, 1]) * rng.integers(10_000, 600_000))      # R$100 a R$6.000
    old = int(df.at[i, "c_fin"]); df.at[i, "c_fin"] = old + delta
    log(i, "E1b", "valor", "saldo_final_2025_brl", old / 100, (old + delta) / 100, delta,
        "saldo final diferente da soma das parcelas (erro de soma/digitação)")
# E2: quantidade registrada diverge da custódia; valores calculados sobre a quantidade errada
for i in pega(350):
    k = float(rng.choice([0.5, 0.8, 1.2, 1.5, 10.0]))
    qo = int(df.at[i, "quantidade_acoes"]); qn = max(1, int(round(qo * k)))
    k_eff = qn / qo
    for c in ("c_ini", "c_eq", "c_oci", "c_jcp", "c_div"):
        df.at[i, c] = int(round(int(df.at[i, c]) * k_eff))
    old_fin = int(df.at[i, "c_fin"])
    df.at[i, "c_fin"] = int(df.loc[i, ["c_ini", "c_eq", "c_oci", "c_jcp", "c_div"]].sum())
    df.at[i, "quantidade_acoes"] = qn
    log(i, "E2", "valor", "quantidade_acoes", qo, qn, int(df.at[i, "c_fin"]) - old_fin,
        f"quantidade registrada ({qn}) diverge do extrato do custodiante ({qo}); valores calculados sobre a quantidade errada")
# E4: lançamento posterior à autorização das DFs (corte)
for i in pega(150):
    nd = pd.Timestamp("2026-03-25") + pd.Timedelta(days=int(rng.integers(0, 40)))
    old = df.at[i, "data_lancamento"]; df.at[i, "data_lancamento"] = nd.strftime("%Y-%m-%d")
    log(i, "E4", "corte", "data_lancamento", old, nd.strftime("%Y-%m-%d"), int(df.at[i, "c_eq"]),
        "equivalência de 2025 lançada após 24/03/2026 (autorização das DFs): risco de corte/ajuste pós-fechamento")
# E5: lançamentos manuais suspeitos (valor redondo, fim de semana, madrugada, usuário não autorizado)
for i in pega(200):
    alvo = int(rng.choice([1_000_000, 2_500_000, 5_000_000, 10_000_000]))     # R$10k..100k (centavos)
    old = int(df.at[i, "c_eq"]); df.at[i, "c_eq"] = alvo; df.at[i, "c_fin"] += alvo - old
    df.at[i, "tipo_lancamento"] = "MANUAL"
    df.at[i, "usuario_lancamento"] = rng.choice(["U99", "U98", "U03", "U05"])
    sab = pd.Timestamp("2026-01-03") + pd.Timedelta(days=int(rng.choice([0, 1, 7, 8, 14, 15])))
    df.at[i, "data_lancamento"] = sab.strftime("%Y-%m-%d")
    df.at[i, "hora_lancamento"] = int(rng.choice([0, 1, 2, 3, 23]))
    log(i, "E5", "valor", "equivalencia_2025_brl", old / 100, alvo / 100, alvo - old,
        "lançamento manual com valor redondo, em fim de semana/madrugada, por usuário atípico (indicador de override)")
# E6: quantidade inválida (zero/negativa) com saldo preservado
for i in pega(60):
    qo = int(df.at[i, "quantidade_acoes"])
    df.at[i, "quantidade_acoes"] = int(rng.choice([0, -qo]))
    log(i, "E6", "integridade", "quantidade_acoes", qo, int(df.at[i, "quantidade_acoes"]), 0,
        "quantidade zero/negativa com saldo positivo (integridade cadastral; sem efeito monetário direto)")
# E7: baixa indevida (saldo zerado)
for i in pega(40):
    old = int(df.at[i, "c_fin"])
    for c in ("c_ini", "c_eq", "c_oci", "c_jcp", "c_div", "c_fin"):
        df.at[i, c] = 0
    log(i, "E7", "valor", "saldo_final_2025_brl", old / 100, 0.0, -old, "lote com saldo zerado indevidamente (subavaliação)")
# E8: classificação em conta contábil indevida
for i in pega(80):
    df.at[i, "conta_contabil"] = "1.1.2.05"     # Dividendos e JCP a receber
    log(i, "E8", "classificacao", "conta_contabil", "1.2.1.01", "1.1.2.05", -int(df.at[i, "c_fin"]),
        "lote classificado em conta indevida (dividendos a receber) — efeito sobre a conta Investimentos é negativo")

# E9: alteração CONSISTENTE no razão e no extrato simulado do custodiante (não localizável linha a linha)
for i in pega(150):
    qo = int(df.at[i, "quantidade_acoes"]); qn = int(round(qo * 1.3)); k_eff = qn / qo
    for c in ("c_ini", "c_eq", "c_oci", "c_jcp", "c_div"):
        df.at[i, c] = int(round(int(df.at[i, c]) * k_eff))
    old_fin = int(df.at[i, "c_fin"])
    df.at[i, "c_fin"] = int(df.loc[i, ["c_ini", "c_eq", "c_oci", "c_jcp", "c_div"]].sum())
    df.at[i, "quantidade_acoes"] = qn; df.at[i, "quantidade_custodia_externa"] = qn
    log(i, "E9", "valor", "quantidade_acoes (razão e custódia)", qo, qn, int(df.at[i, "c_fin"]) - old_fin,
        "quantidade e valores majorados em 30% de forma consistente no razão E no extrato do custodiante — "
        "só aparece no total de controle de ações (não localizável por comparação linha a linha)")

# ------------------------------------------------------------------ 5. duplicidades (E3) e ordenação final
dup_idx = rng.choice(np.setdiff1d(np.arange(N_LIMPOS), perm[:pos]), size=N_DUPL, replace=False)
dups = df.loc[dup_idx].copy()
for i in dup_idx:
    log(len(df) + len(reg), "E3", "valor", "id_lote", df.at[i, "id_lote"], df.at[i, "id_lote"],
        int(df.at[i, "c_fin"]), "registro duplicado (mesmo lote lançado duas vezes com novo id_registro)")
df["_orig"] = np.arange(N_LIMPOS); dups["_orig"] = -1 - np.arange(N_DUPL)
full = pd.concat([df, dups], ignore_index=True)
full = full.sample(frac=1.0, random_state=P.SEED).reset_index(drop=True)
full.insert(0, "id_registro", [f"SINT-{i:07d}" for i in range(1, len(full) + 1)])

# mapa índice-original -> id_registro (para o gabarito); duplicatas identificadas por _orig negativo
mapa = {int(o): r for o, r in zip(full["_orig"], full["id_registro"]) if o >= 0}
mapa_dup = {int(o): r for o, r in zip(full["_orig"], full["id_registro"]) if o < 0}
gab = pd.DataFrame(reg)
ids = []
n_dup_seen = 0
for _, r in gab.iterrows():
    if r["tipo_erro"] == "E3":
        n_dup_seen += 1
        ids.append(mapa_dup[-n_dup_seen])
    else:
        ids.append(mapa[int(r["indice"])])
gab.insert(0, "id_registro", ids)
gab = gab.drop(columns=["indice"])
full = full.drop(columns=["_orig"])

# ------------------------------------------------------------------ 6. formato final
def brl(c):  # centavos -> reais com 2 casas
    return (c.astype(np.int64) / 100).round(2)


out = pd.DataFrame(dict(
    id_registro=full["id_registro"], id_lote=full["id_lote"], custodiante=full["custodiante"],
    data_origem=full["data_origem"], conta_contabil=full["conta_contabil"],
    quantidade_acoes=full["quantidade_acoes"], quantidade_custodia_externa=full["quantidade_custodia_externa"],
    saldo_inicial_2025_brl=brl(full["c_ini"]), equivalencia_2025_brl=brl(full["c_eq"]),
    reflexo_oci_2025_brl=brl(full["c_oci"]), jcp_bruto_2025_brl=brl(full["c_jcp"]),
    dividendos_2025_brl=brl(full["c_div"]), saldo_final_2025_brl=brl(full["c_fin"]),
    data_lancamento=full["data_lancamento"],
    hora_lancamento=full["hora_lancamento"].astype(int).astype(str).str.zfill(2) + ":" +
                    full["minuto"].astype(int).astype(str).str.zfill(2) + ":" +
                    full["segundo"].astype(int).astype(str).str.zfill(2),
    usuario_lancamento=full["usuario_lancamento"], tipo_lancamento=full["tipo_lancamento"],
    origem_dado="SINTETICO",
))
csv = os.path.join(OUT, "base_investimento_vale_sintetica.csv")
out.to_csv(csv, index=False)
with open(csv, "rb") as fi, open(csv + ".gz", "wb") as raw:
    with gzip.GzipFile(filename="", mode="wb", fileobj=raw, compresslevel=9, mtime=0) as fo:   # mtime=0 -> hash reprodutível
        shutil.copyfileobj(fi, fo)
gab.to_csv(os.path.join(OUT, "registro_erros_inseridos.csv"), index=False)

dic = pd.DataFrame([
    ("id_registro", "texto", "—", "Identificador único da linha (prefixo SINT- = dado sintético).", "Gerado", "Chave primária"),
    ("id_lote", "texto", "—", "Identificador do sublote de custódia de ações da Vale (fictício). Repetido apenas nas duplicidades inseridas.", "Gerado", "Único, exceto erro E3"),
    ("custodiante", "texto", "—", "Código fictício do agente de custódia (C01–C06).", "Hipótese A3", "Lista fechada"),
    ("data_origem", "data", "AAAA-MM-DD", "Data fictícia de formação do sublote (01/08/2017–31/12/2024).", "Hipótese A3", "<= 2024-12-31"),
    ("conta_contabil", "texto", "—", "Conta contábil do razão auxiliar. 1.2.1.01 = Investimentos em coligada (Vale).", "Hipótese A4", "Deve ser 1.2.1.01"),
    ("quantidade_acoes", "inteiro", "ações", "Quantidade registrada de ações ordinárias VALE3 do sublote. Soma (limpa) = 163.355.000.", "DFP/CVM (total); alocação sintética", "> 0"),
    ("quantidade_custodia_externa", "inteiro", "ações", "Quantidade segundo extrato SIMULADO do custodiante (para PT 505).", "Sintético", "= quantidade_acoes"),
    ("saldo_inicial_2025_brl", "decimal", "R$", "Saldo do sublote em 31/12/2024. Soma (limpa) = R$ 8.153.681.000,00.", "Balanço 2024 (total); alocação pro rata", "pro rata da quantidade"),
    ("equivalencia_2025_brl", "decimal", "R$", "Equivalência patrimonial 2025 do sublote. Soma (limpa) = R$ 571.264.000,00.", "DRE 2025 / Nota 8", "pro rata da quantidade"),
    ("reflexo_oci_2025_brl", "decimal", "R$", "Reflexos de empresas com influência significativa (OCI) 2025. Soma (limpa) = −R$ 135.589.000,00.", "DMPL / DRA 2025", "pro rata da quantidade"),
    ("jcp_bruto_2025_brl", "decimal", "R$", "JCP declarados pela Vale (bruto de IRRF) em 2025: recebidos + a receber. Soma (limpa) = −R$ 566.011.000,00.", "Nota 13", "pro rata da quantidade"),
    ("dividendos_2025_brl", "decimal", "R$", "Dividendos declarados pela Vale em 2025: recebidos + a receber. Soma (limpa) = −R$ 678.589.000,00.", "Nota 13", "pro rata da quantidade"),
    ("saldo_final_2025_brl", "decimal", "R$", "Saldo do sublote em 31/12/2025 = soma das 5 parcelas anteriores. Soma (limpa) = R$ 7.344.756.000,00.", "Balanço 2025 / Nota 8", "= soma das parcelas"),
    ("data_lancamento", "data", "AAAA-MM-DD", "Data (sintética) do lançamento contábil da equivalência 2025 do sublote.", "Hipótese A5", "Entre 2025-12-31 e 2026-03-24"),
    ("hora_lancamento", "hora", "HH:MM:SS", "Hora (sintética) do lançamento.", "Hipótese A5", "—"),
    ("usuario_lancamento", "texto", "—", "SISTEMA (rotina automática) ou U01–U08 (usuários autorizados fictícios). U98/U99 = não autorizados (só nos erros).", "Hipótese A5", "Lista de autorizados"),
    ("tipo_lancamento", "texto", "—", "AUTOMATICO ou MANUAL.", "Hipótese A5", "—"),
    ("origem_dado", "texto", "—", "Sempre 'SINTETICO' — rótulo explícito de dado fictício.", "Gerado", "Constante"),
], columns=["variavel", "tipo", "unidade", "descricao", "fonte_ou_hipotese", "regra_de_validacao"])
dic.to_csv(os.path.join(OUT, "dicionario_variaveis.csv"), index=False)

# hashes
with open(os.path.join(OUT, "hashes.txt"), "w") as fh:
    for nome in ("base_investimento_vale_sintetica.csv", "base_investimento_vale_sintetica.csv.gz",
                 "registro_erros_inseridos.csv"):
        h = hashlib.sha256(open(os.path.join(OUT, nome), "rb").read()).hexdigest()
        fh.write(f"{h}  {nome}\n")
print("linhas:", len(out), "| soma saldo final (R$):", f"{out.saldo_final_2025_brl.sum():,.2f}",
      "| erros inseridos:", len(gab))
print(gab.groupby("tipo_erro").agg(n=("id_registro", "size"), efeito=("efeito_saldo_brl", "sum")))
