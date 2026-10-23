#!/usr/bin/env python3
"""Figuras do PT-450 (erros inseridos x detectados). Dados sintéticos."""
import os, pandas as pd, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
R=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
t=pd.read_csv(os.path.join(R,"saidas","comparacao_inserido_vs_detectado.csv")); t=t[t.tipo_erro!="TOTAL"]
fig,ax=plt.subplots(1,2,figsize=(9,3.6))
x=range(len(t)); w=.38
ax[0].bar([i-w/2 for i in x],t.inseridos,w,color="#9aa5b1",label="Inseridos")
ax[0].bar([i+w/2 for i in x],t.detectados_populacao,w,color="#1f5fa8",label="Detectados (100%)")
ax[0].set_xticks(list(x)); ax[0].set_xticklabels(t.tipo_erro,fontsize=8); ax[0].set_title("Registros por tipo de erro",fontsize=10); ax[0].legend(fontsize=8,frameon=False)
ax[1].bar(t.tipo_erro,t.efeito_inserido_brl/1e6,color=["#1f5fa8" if v>=0 else "#c0562b" for v in t.efeito_inserido_brl])
ax[1].axhline(0,color="#444",lw=.6); ax[1].set_title("Efeito no saldo (R$ milhões)",fontsize=10); ax[1].tick_params(labelsize=8)
for a in ax:
    a.spines[["top","right"]].set_visible(False)
fig.text(.5,.01,"Dados SINTÉTICOS — E2 e E5 concentram o efeito; E9 não é localizável por linha",ha="center",fontsize=8)
plt.tight_layout(rect=(0,.04,1,1)); plt.savefig(os.path.join(R,"saidas","fig_inseridos_detectados.png"),dpi=160)
