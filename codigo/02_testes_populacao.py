#!/usr/bin/env python3
"""
02_testes_populacao.py — Testes de auditoria sobre 100% da base SINTÉTICA (PT 240, 500, 520, 530, 450).

IMPORTANTE: este script NÃO lê registro_erros_inseridos.csv (o gabarito). Os testes usam apenas
(i) a base, (ii) totais públicos das DFs (parametros.py) e (iii) o extrato SIMULADO do custodiante
(coluna quantidade_custodia_externa). A comparação com o gabarito é feita em 04_comparacao.py.

Saídas em saidas/: excecoes_populacao.csv, resumo_testes_populacao.csv, conciliacao_razao_balanco.csv
Classificação de todos os procedimentos deste script: "Simulado para fins didáticos".
"""
import os, sys, gzip
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(__file__))
import parametros as P

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SAIDAS = os.path.join(RAIZ, "saidas"); os.makedirs(SAIDAS, exist_ok=True)
ARQ = os.path.join(RAIZ, "base_simulada", "base_investimento_vale_sintetica.csv.gz")

df = pd.read_csv(ARQ)
MONEY = ["saldo_inicial_2025_brl", "equivalencia_2025_brl", "reflexo_oci_2025_brl",
         "jcp_bruto_2025_brl", "dividendos_2025_brl", "saldo_final_2025_brl"]
for c in MONEY:
    df["c_" + c] = np.rint(df[c].to_numpy() * 100).astype(np.int64)

Q = P.QTD_ACOES
tot = {"saldo_inicial_2025_brl": P.SALDO_INICIAL, "equivalencia_2025_brl": P.EQUIVALENCIA,
       "reflexo_oci_2025_brl": P.OCI_REFLEXO, "jcp_bruto_2025_brl": P.JCP_BRUTO,
       "dividendos_2025_brl": P.DIVIDENDOS}
q, qc = df["quantidade_acoes"].to_numpy(), df["quantidade_custodia_externa"].to_numpy()

# valor esperado por parcela = total público × (quantidade da CUSTÓDIA / total de ações)   [centavos]
exp = {c: (2 * int(v) * 100 * qc + Q) // (2 * Q) for c, v in tot.items()}   # arredondamento ao centavo mais próximo
exp_fin = sum(exp.values())
parts = sum(df["c_" + c].to_numpy() for c in tot)
c_fin = df["c_saldo_final_2025_brl"].to_numpy()

TOL = 10          # 10 centavos (arredondamento da alocação pro rata)
flags = pd.DataFrame(index=df.index)
flags["T1_soma"] = np.abs(c_fin - parts) > TOL
flags["T2_qtd_vs_custodia"] = q != qc
flags["T3_duplicidade_lote"] = df.duplicated("id_lote", keep="first")
flags["T4_qtd_invalida"] = q <= 0
pro = np.zeros(len(df), dtype=bool)
for c in tot:
    pro |= np.abs(df["c_" + c].to_numpy() - exp[c]) > 5
flags["T5_prorata_recalculo"] = pro & (q == qc) & ~flags["T3_duplicidade_lote"]
flags["T6_corte_pos_emissao"] = df["data_lancamento"] > P.DATA_EMISSAO_DF
dt = pd.to_datetime(df["data_lancamento"])
hh = df["hora_lancamento"].str.slice(0, 2).astype(int)
manual = df["tipo_lancamento"] == "MANUAL"
autorizados = {f"U{i:02d}" for i in range(1, 9)} | {"SISTEMA"}
flags["T7a_manual_fim_semana"] = manual & (dt.dt.dayofweek >= 5)
flags["T7b_manual_madrugada"] = manual & ((hh < 6) | (hh >= 22))
flags["T7c_usuario_nao_autorizado"] = ~df["usuario_lancamento"].isin(autorizados)
eq_c = df["c_equivalencia_2025_brl"].to_numpy()
flags["T7d_valor_redondo"] = (eq_c >= 500_000) & (eq_c % 500_000 == 0)     # múltiplos exatos de R$ 5.000,00
flags["T8_saldo_zero_com_qtd"] = (c_fin == 0) & (q > 0)
flags["T9_conta_indevida"] = df["conta_contabil"] != "1.2.1.01"

teste_cols = list(flags.columns)
flags["qualquer"] = flags[teste_cols].any(axis=1)

# efeito monetário estimado (saldo registrado − saldo esperado pela custódia); duplicidade: valor integral
efeito = c_fin - exp_fin
efeito = np.where(flags["T3_duplicidade_lote"], c_fin, efeito)
df["efeito_estimado_cents"] = efeito
m_t3 = flags["T3_duplicidade_lote"].to_numpy()
# T0: total de controle de ações (exclui duplicidades): excesso de ações em relação ao total público
excesso_acoes = int(qc[~m_t3].sum() - Q)
preco_medio = P.SALDO_FINAL / Q
efeito_t0 = excesso_acoes * preco_medio
prio = ["T3_duplicidade_lote", "T9_conta_indevida", "T4_qtd_invalida", "T2_qtd_vs_custodia", "T8_saldo_zero_com_qtd",
        "T1_soma", "T5_prorata_recalculo", "T7d_valor_redondo", "T7c_usuario_nao_autorizado",
        "T7a_manual_fim_semana", "T7b_manual_madrugada", "T6_corte_pos_emissao"]
primario = pd.Series("", index=df.index)
for t in reversed(prio):
    primario = np.where(flags[t], t, primario)
df["teste_primario"] = primario
df["testes_acionados"] = flags[teste_cols].apply(lambda r: "|".join([c for c in teste_cols if r[c]]), axis=1) \
    if flags["qualquer"].sum() < 50_000 else ""
sel = flags["qualquer"]
# tabela de exceções (apenas linhas com algum alerta)
exc = df.loc[sel, ["id_registro", "id_lote", "teste_primario", "testes_acionados", "quantidade_acoes",
                   "quantidade_custodia_externa", "saldo_final_2025_brl", "efeito_estimado_cents",
                   "data_lancamento", "hora_lancamento", "usuario_lancamento", "tipo_lancamento", "conta_contabil"]].copy()
exc["efeito_estimado_brl"] = (exc["efeito_estimado_cents"] / 100).round(2)
# efeito só tem sentido monetário para erros de valor; corte/integridade/JE sem desvio de valor ficam ~0
exc = exc.drop(columns=["efeito_estimado_cents"])
exc.to_csv(os.path.join(SAIDAS, "excecoes_populacao.csv"), index=False)

# resumo por teste
linhas = []
for t in teste_cols:
    m = flags[t].to_numpy()
    linhas.append(dict(teste=t, registros_alertados=int(m.sum()),
                       soma_saldo_alertado_brl=round(c_fin[m].sum() / 100, 2),
                       efeito_estimado_brl=round(efeito[m].sum() / 100, 2)))
linhas.append(dict(teste="T0_total_controle_acoes", registros_alertados=0, soma_saldo_alertado_brl=0.0, efeito_estimado_brl=round(efeito_t0, 2)))
res = pd.DataFrame(linhas)
res.to_csv(os.path.join(SAIDAS, "resumo_testes_populacao.csv"), index=False)

# conciliação razão auxiliar × balanço (PT 500)
fin = c_fin.sum() / 100
gl = P.SALDO_FINAL
m_t3 = flags["T3_duplicidade_lote"].to_numpy()
m_conta = flags["T9_conta_indevida"].to_numpy()
rest = ~m_t3 & ~m_conta
comp = {
    "Duplicidades (T3)": efeito[m_t3].sum() / 100,
    "Quantidade diverge da custódia (T2)": efeito[flags["T2_qtd_vs_custodia"].to_numpy() & rest].sum() / 100,
    "Valor sem aderência ao pro rata / soma (T1, T5, T8) exceto T2": efeito[~flags["T2_qtd_vs_custodia"].to_numpy() & rest].sum() / 100,
}
conc = [("Saldo contábil — Balanço 31/12/2025 (Investimentos)", gl),
        ("(+) Duplicidades (T3)", comp["Duplicidades (T3)"]),
        ("(+/−) Quantidade registrada diverge da custódia (T2)", comp["Quantidade diverge da custódia (T2)"]),
        ("(+/−) Valores sem aderência ao pro rata/soma (T1, T5, T8)", comp["Valor sem aderência ao pro rata / soma (T1, T5, T8) exceto T2"]),
        (f"(+) Excesso de ações no total de controle (T0): {excesso_acoes:,} ações × R$ {preco_medio:,.4f} — NÃO localizado por linha", efeito_t0),
        ]
soma_expl = sum(v for _, v in conc[1:])
conc.append(("Total: saldo esperado do razão auxiliar (todas as contas)", gl + soma_expl))
conc.append(("Soma observada do razão auxiliar (todas as contas)", fin))
conc.append(("Diferença residual não explicada (arredondamento/precisão)", round(fin - (gl + soma_expl), 2)))
soma_c = c_fin[m_conta].sum() / 100
conc.append(("(−) Registros em conta indevida (T9)", -soma_c))
conc.append(("Total: soma do razão auxiliar na conta 1.2.1.01", fin - soma_c))
conc.append(("Diferença total da conta 1.2.1.01 vs. Balanço", fin - soma_c - gl))
pd.DataFrame(conc, columns=["item", "valor_brl"]).round(2).to_csv(os.path.join(SAIDAS, "conciliacao_razao_balanco.csv"), index=False)

# totais de controle
ctrl = dict(registros=len(df), soma_quantidade=int(q.sum()), soma_quantidade_custodia=int(qc.sum()),
            soma_saldo_final=fin, saldo_balanco=gl, diferenca=round(fin - gl, 2),
            registros_com_alerta=int(sel.sum()))
pd.Series(ctrl).to_csv(os.path.join(SAIDAS, "totais_controle.csv"), header=["valor"])
print(pd.Series(ctrl))
print(res.to_string(index=False))
print(pd.DataFrame(conc, columns=["item", "valor_brl"]).round(2).to_string(index=False))
