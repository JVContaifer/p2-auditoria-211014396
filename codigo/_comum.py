"""Utilitários comuns da geração dos papéis de trabalho (formatação pt-BR, carga de resultados, rótulos)."""
import os
import pandas as pd

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
S = os.path.join(RAIZ, "saidas")
MAT = "211014396"
DATA_PREP = "23/10/2026"

RP = "Realizado com evidência pública"
PLN = "Planejado por falta de acesso"
SIM = "Simulado para fins didáticos"


def n0(x):
    """inteiro com ponto de milhar"""
    return f"{x:,.0f}".replace(",", ".")


def n2(x):
    return f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def brl(x):
    return "R$ " + n2(x)


def mil(x):
    """valor em R$ mil"""
    return "R$ " + n0(x) + " mil"


def pct(x, d=1):
    return f"{x * 100:.{d}f}".replace(".", ",") + "%"


def carregar():
    """Carrega os resultados dos scripts 02–04 e devolve dicionários prontos para uso nos textos."""
    V = {}
    ctrl = pd.read_csv(os.path.join(S, "totais_controle.csv"), index_col=0)["valor"]
    V["n_reg"] = int(ctrl["registros"])
    V["soma_razao"] = float(ctrl["soma_saldo_final"])
    V["saldo_bal"] = float(ctrl["saldo_balanco"])
    V["dif_total"] = float(ctrl["diferenca"])
    V["alertas"] = int(ctrl["registros_com_alerta"])
    mus = pd.read_csv(os.path.join(S, "mus_resumo.csv"))
    M = dict(zip(mus["parametro_ou_resultado"], mus["valor"]))
    V["mus"] = M
    V["mus_n"] = int(float(M["Itens na amostra (total)"]))
    V["mus_J"] = float(M["Intervalo de amostragem (R$)"])
    V["mus_uel"] = float(M["Limite superior de erro (Stringer, 95%) — superavaliação (R$)"])
    V["mus_mle"] = float(M["Distorção mais provável projetada — superavaliação (R$)"])
    V["mus_bruta"] = float(M["Distorção bruta encontrada na amostra (R$)"])
    V["mus_inicio"] = float(M["Início aleatório (R$)"])
    V["mus_pop"] = float(M["Valor contábil da população (R$)"])
    V["mus_concl"] = M["Conclusão da amostra"]
    V["mus_ratio"] = float(M["UEL / distorção tolerável"])
    cr = pd.read_csv(os.path.join(S, "comparacao_resumo.csv"), index_col=0)["valor"]
    V["cmp"] = cr
    V["efeito_liq"] = float(cr["efeito_liquido_inserido_valor"])
    V["super_bruta"] = float(cr["superavaliacao_bruta"])
    V["sub_bruta"] = float(cr["subavaliacao_bruta"])
    V["n_erros"] = int(cr["erros_inseridos"])
    V["n_nao_det"] = int(cr["nao_detectados_linha_a_linha"])
    V["cmp_tab"] = pd.read_csv(os.path.join(S, "comparacao_inserido_vs_detectado.csv"))
    V["conc"] = pd.read_csv(os.path.join(S, "conciliacao_razao_balanco.csv"))
    V["testes"] = pd.read_csv(os.path.join(S, "resumo_testes_populacao.csv"))
    V["mus_erros"] = pd.read_csv(os.path.join(S, "mus_erros_na_amostra.csv"))
    return V


def tabela_md(df, fmt=None):
    """DataFrame -> tabela markdown (pipe). fmt: dict col->callable."""
    fmt = fmt or {}
    cols = list(df.columns)
    linhas = ["| " + " | ".join(cols) + " |", "|" + "|".join(["---"] * len(cols)) + "|"]
    for _, r in df.iterrows():
        cel = []
        for c in cols:
            v = r[c]
            cel.append(fmt[c](v) if c in fmt else ("" if pd.isna(v) else str(v)))
        linhas.append("| " + " | ".join(cel) + " |")
    return "\n".join(linhas)


def tab(cab, linhas):
    """Cabeçalho (lista) + linhas (lista de listas) -> tabela pipe do pandoc com larguras relativas (pelo comprimento do conteúdo)."""
    import math
    rows = [[str(x).replace("|", "/").replace("\n", " ") for x in l] for l in linhas]
    larg = []
    for j, h in enumerate(cab):
        m = max([len(str(h))] + [len(r[j]) for r in rows if j < len(r)])
        larg.append(max(len(str(h)) * 1.4, 6, min(60, math.sqrt(m) * 6)))
    tot = sum(larg)
    sep = ["-" * max(3, int(round(100 * w / tot))) for w in larg]
    out = ["| " + " | ".join(cab) + " |", "|" + "|".join(sep) + "|"]
    for r in rows:
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out)


def pt(code, titulo, norma, itens, objetivo, assercoes, populacao, procs, evidencias, resultados, conclusao, limitacoes, classes=None):
    """Estrutura de um papel de trabalho. procs: lista de (ref, descrição, classificação, status)."""
    return dict(code=code, titulo=titulo, norma=norma, itens=itens, objetivo=objetivo, assercoes=assercoes,
                populacao=populacao, procs=procs, evidencias=evidencias, resultados=resultados,
                conclusao=conclusao, limitacoes=limitacoes)


def render(p):
    """Renderiza um PT em markdown com todos os campos exigidos."""
    classes = sorted({c for _, _, c, _ in p["procs"]})
    cab = f"""# {p['code']} — {p['titulo']}

| Campo | Conteúdo |
|---|---|
| **Código** | {p['code']} |
| **Título** | {p['titulo']} |
| **Norma e itens utilizados** | {p['norma']} — {p['itens']} |
| **Entidade / período** | Bradespar S.A. (CNPJ 03.847.461/0001-92) — exercício findo em 31/12/2025 (comparativo 2024) |
| **Preparado por** | Matrícula {MAT} — {DATA_PREP} |
| **Revisão** | Revisor: ____________ · Data: ____/____/______ *(campo reservado; nenhuma assinatura ou revisão é simulada)* |
| **Classificações presentes neste PT** | {'; '.join(classes)} |

> **Aviso:** trabalho acadêmico individual (UnB). Não é auditoria real, não houve contato com a companhia ou seu auditor, e este papel não expressa opinião de auditoria. Dados da base de lotes são **SINTÉTICOS**.

## 1. Objetivo e conta / processo / divulgação
{p['objetivo']}

## 2. Asserções relevantes e riscos
{p['assercoes']}

## 3. População, fontes e critérios de seleção
{p['populacao']}

## 4. Procedimentos planejados e executados
{tab(['Ref.', 'Procedimento', 'Classificação', 'Situação'], p['procs'])}

## 5. Evidências e referências cruzadas
{p['evidencias']}

## 6. Resultados e exceções
{p['resultados']}

## 7. Conclusão
{p['conclusao']}

## 8. Limitações
{p['limitacoes']}
"""
    return cab
