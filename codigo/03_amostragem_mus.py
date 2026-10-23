#!/usr/bin/env python3
"""
03_amostragem_mus.py — Amostragem por Unidade Monetária (MUS) sobre a base SINTÉTICA (PT 530).
Classificação dos procedimentos: "Simulado para fins didáticos".

Fluxo: (1) parâmetros de materialidade (PT 320) -> (2) tamanho da amostra -> (3) estrato de itens
individualmente significativos -> (4) seleção sistemática com início aleatório (semente = matrícula+1)
-> (5) testes de detalhe em cada item (mesmos procedimentos T1–T9 de 02_testes_populacao.py, aplicados item a item)
-> (6) projeção de distorções e limite superior de erro (Stringer) -> (7) comparação com a materialidade para execução.
"""
import os, sys, math
import numpy as np
import pandas as pd
from scipy.stats import chi2

sys.path.insert(0, os.path.dirname(__file__))
import parametros as P

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SAIDAS = os.path.join(RAIZ, "saidas"); PLAN = os.path.join(RAIZ, "planilhas")
os.makedirs(PLAN, exist_ok=True)

# ---------------- parâmetros (PT 320) ----------------
MAT_GLOBAL = 80_000_000.0         # 1% do ativo total (R$ 7.999.560 mil) arredondado
MAT_EXEC = 0.70 * MAT_GLOBAL      # materialidade para execução (70%)
TRIVIAL = 0.05 * MAT_GLOBAL       # limite de claramente trivial (5%)
TM = MAT_EXEC                     # distorção tolerável
EM = 5_000_000.0                  # distorção esperada (HIPÓTESE didática, sem base histórica pública)
CONF = 0.95
RF0 = chi2.ppf(CONF, 2) / 2       # = 2,9957 (Poisson, zero erros)
EF = 1.6                          # fator de expansão (95%)

df = pd.read_csv(os.path.join(RAIZ, "base_simulada", "base_investimento_vale_sintetica.csv.gz"),
                 usecols=["id_registro", "id_lote", "saldo_final_2025_brl", "conta_contabil"])
exc = pd.read_csv(os.path.join(SAIDAS, "excecoes_populacao.csv"))
efeito = exc.set_index("id_registro")["efeito_estimado_brl"]
testes = exc.set_index("id_registro")["teste_primario"]

pop = df[df["saldo_final_2025_brl"] > 0].reset_index(drop=True)      # MUS exige valores positivos
BV = pop["saldo_final_2025_brl"].sum()
n_calc = math.ceil(BV * RF0 / (TM - EM * EF))
J = BV / n_calc
topo = pop[pop["saldo_final_2025_brl"] >= J]
resto = pop[pop["saldo_final_2025_brl"] < J].reset_index(drop=True)
BV_r = resto["saldo_final_2025_brl"].sum()
n_r = math.ceil(BV_r / J)

rng = np.random.default_rng(P.SEED + 1)
inicio = rng.uniform(0, J)
pontos = inicio + J * np.arange(n_r)
cum = resto["saldo_final_2025_brl"].cumsum().to_numpy()
pontos = pontos[pontos < cum[-1]]
idx = np.unique(np.searchsorted(cum, pontos, side="left"))
amostra = pd.concat([topo.assign(estrato="Topo (>= intervalo)"), resto.loc[idx].assign(estrato="MUS sistemática")],
                    ignore_index=True)
amostra["teste_primario_detectado"] = amostra["id_registro"].map(testes).fillna("")
amostra["distorcao_brl"] = amostra["id_registro"].map(efeito).fillna(0.0)
# classificação de natureza: apenas erros com efeito monetário entram na projeção
amostra["tainting"] = np.where(amostra["estrato"].eq("MUS sistemática"),
                               amostra["distorcao_brl"] / amostra["saldo_final_2025_brl"], np.nan)
amostra.to_csv(os.path.join(PLAN, "amostra_MUS.csv"), index=False)

# ---------------- avaliação ----------------
erros = amostra[amostra["distorcao_brl"].abs() > 0.5]
sup = erros[erros["distorcao_brl"] > 0]
inf = erros[erros["distorcao_brl"] < 0]
topo_err = sup[sup["estrato"].str.startswith("Topo")]["distorcao_brl"].sum()
t_sorted = np.sort(np.clip(sup[sup["estrato"].eq("MUS sistemática")]["tainting"].to_numpy(), 0, 1))[::-1]
mle = float((t_sorted * J).sum())
uel = RF0 * J
rf_prev = RF0
for k, t in enumerate(t_sorted, start=1):
    rf_k = chi2.ppf(CONF, 2 * (k + 1)) / 2
    uel += (rf_k - rf_prev) * t * J
    rf_prev = rf_k
uel += topo_err
linhas = [
    ("Valor contábil da população (R$)", BV), ("Materialidade global (R$)", MAT_GLOBAL),
    ("Materialidade para execução = distorção tolerável (R$)", TM), ("Distorção esperada assumida (R$)", EM),
    ("Fator de confiança (zero erros), 95%", round(RF0, 4)), ("Fator de expansão", EF),
    ("Tamanho calculado da amostra", n_calc), ("Intervalo de amostragem (R$)", round(J, 2)),
    ("Itens do estrato topo (>= intervalo)", len(topo)), ("Itens selecionados no estrato sistemático", len(idx)),
    ("Itens na amostra (total)", len(amostra)), ("Início aleatório (R$)", round(inicio, 2)),
    ("Itens com distorção (superavaliação)", len(sup)), ("Itens com distorção (subavaliação)", len(inf)),
    ("Distorção bruta encontrada na amostra (R$)", round(erros["distorcao_brl"].sum(), 2)),
    ("Distorção mais provável projetada — superavaliação (R$)", round(mle + topo_err, 2)),
    ("Limite superior de erro (Stringer, 95%) — superavaliação (R$)", round(uel, 2)),
    ("UEL / distorção tolerável", round(uel / TM, 3)),
    ("Conclusão da amostra", "UEL <= TM: amostra apoia aceitação" if uel <= TM else "UEL > TM: amostra NÃO apoia aceitação sem ajustes/ampliação"),
]
pd.DataFrame(linhas, columns=["parametro_ou_resultado", "valor"]).to_csv(os.path.join(SAIDAS, "mus_resumo.csv"), index=False)
erros[["id_registro", "estrato", "saldo_final_2025_brl", "distorcao_brl", "tainting", "teste_primario_detectado"]] \
    .to_csv(os.path.join(SAIDAS, "mus_erros_na_amostra.csv"), index=False)
print(pd.DataFrame(linhas, columns=["p", "v"]).to_string(index=False))
print(erros[["id_registro", "estrato", "saldo_final_2025_brl", "distorcao_brl", "teste_primario_detectado"]].to_string(index=False))
