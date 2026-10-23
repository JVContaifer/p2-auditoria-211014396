#!/usr/bin/env python3
"""
04_comparacao.py — Compara o GABARITO (registro_erros_inseridos.csv) com o que foi DETECTADO
pelos testes de população (02) e pela amostra MUS (03).  Alimenta PT 450, 500, 530.
Só este script lê o gabarito.  Classificação: "Simulado para fins didáticos".
"""
import os, sys
import pandas as pd
sys.path.insert(0, os.path.dirname(__file__))
RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
S = os.path.join(RAIZ, "saidas")
gab = pd.read_csv(os.path.join(RAIZ, "base_simulada", "registro_erros_inseridos.csv"))
exc = pd.read_csv(os.path.join(S, "excecoes_populacao.csv"))
am = pd.read_csv(os.path.join(RAIZ, "planilhas", "amostra_MUS.csv"))

base = pd.read_csv(os.path.join(RAIZ, "base_simulada", "base_investimento_vale_sintetica.csv.gz"), usecols=["id_registro", "id_lote"])
lote = base.set_index("id_registro")["id_lote"]
det_pop = set(exc["id_registro"])
# Duplicidade (E3): os dois registros do par são idênticos; considera-se detectado se o LOTE foi sinalizado (T3)
lotes_t3 = set(exc.loc[exc["teste_primario"].eq("T3_duplicidade_lote"), "id_registro"].map(lote))
det_sample = set(am.loc[am["distorcao_brl"].abs() > 0.5, "id_registro"])
in_sample = set(am["id_registro"])
gab["detectado_populacao"] = gab["id_registro"].isin(det_pop)
e3 = gab["tipo_erro"].eq("E3")
gab.loc[e3, "detectado_populacao"] = gab.loc[e3, "id_registro"].map(lote).isin(lotes_t3)
gab["selecionado_na_amostra"] = gab["id_registro"].isin(in_sample)
gab["detectado_na_amostra"] = gab["id_registro"].isin(det_sample)
gab.to_csv(os.path.join(S, "gabarito_vs_detectado_linha_a_linha.csv"), index=False)

t = gab.groupby("tipo_erro").agg(
    inseridos=("id_registro", "size"), natureza=("natureza", "first"),
    efeito_inserido_brl=("efeito_saldo_brl", "sum"),
    detectados_populacao=("detectado_populacao", "sum"),
    selecionados_amostra=("selecionado_na_amostra", "sum"),
    detectados_amostra=("detectado_na_amostra", "sum")).reset_index()
t["recall_populacao_%"] = (100 * t["detectados_populacao"] / t["inseridos"]).round(1)
t["efeito_inserido_brl"] = t["efeito_inserido_brl"].round(2)
tot = {c: t[c].sum() for c in ["inseridos", "efeito_inserido_brl", "detectados_populacao", "selecionados_amostra", "detectados_amostra"]}
tot.update(tipo_erro="TOTAL", natureza="", **{"recall_populacao_%": round(100 * tot["detectados_populacao"] / tot["inseridos"], 1)})
t = pd.concat([t, pd.DataFrame([tot])], ignore_index=True)
t.to_csv(os.path.join(S, "comparacao_inserido_vs_detectado.csv"), index=False)

# falsos positivos: alertas que não estão no gabarito
ids_gab = set(gab["id_registro"])
lotes_e3 = set(gab.loc[e3, "id_registro"].map(lote))
fp = {i for i in det_pop - ids_gab if lote[i] not in lotes_e3}
# efeito líquido por categoria
val = gab[gab["natureza"].eq("valor")]
resumo = dict(
    erros_inseridos=len(gab), alertas_populacao=len(det_pop), falsos_positivos=len(fp),
    nao_detectados_linha_a_linha=int((~gab["detectado_populacao"]).sum()),
    efeito_liquido_inserido_valor=round(val["efeito_saldo_brl"].sum(), 2),
    superavaliacao_bruta=round(val.loc[val["efeito_saldo_brl"] > 0, "efeito_saldo_brl"].sum(), 2),
    subavaliacao_bruta=round(val.loc[val["efeito_saldo_brl"] < 0, "efeito_saldo_brl"].sum(), 2),
    itens_da_amostra=len(in_sample), erros_na_amostra=int(gab["selecionado_na_amostra"].sum()),
    erros_detectados_pela_amostra=int(gab["detectado_na_amostra"].sum()))
pd.Series(resumo).to_csv(os.path.join(S, "comparacao_resumo.csv"), header=["valor"])
print(t.to_string(index=False)); print(pd.Series(resumo))
