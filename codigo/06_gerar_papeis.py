#!/usr/bin/env python3
"""
06_gerar_papeis.py — Gera os 27 papéis de trabalho (markdown), a matriz de cobertura, o registro de fontes,
o registro de versões das normas, os programas por ciclo, a conclusão integrada e o texto-base do dossiê.
Todos os números vêm dos resultados dos scripts 01–05 (nada é digitado à mão nos totais da base sintética).
"""
import os, sys, hashlib, glob
import pandas as pd

sys.path.insert(0, os.path.dirname(__file__))
from _comum import *
import _papeis_a, _papeis_b, _papeis_c

V = carregar()
os.makedirs(os.path.join(RAIZ, "papeis_trabalho"), exist_ok=True)
os.makedirs(os.path.join(RAIZ, "docs"), exist_ok=True)
os.makedirs(os.path.join(RAIZ, "dossie"), exist_ok=True)

todos = {p["code"]: p for p in (_papeis_a.build(V) + _papeis_b.build(V) + _papeis_c.build(V))}

# ---------------------------------------------------------------- índice (PT-230) calculado a partir dos demais PTs
ORDEM = ["PT-EC", "PT-200", "PT-210", "PT-220", "PT-230", "PT-240", "PT-250", "PT-260", "PT-265", "PT-300", "PT-315", "PT-320", "PT-330",
         "PT-402", "PT-450", "PT-500", "PT-501", "PT-505", "PT-510", "PT-520", "PT-530", "PT-540", "PT-550", "PT-560", "PT-570", "PT-580", "PT-600"]
VERS = {  # versões conforme página do CFC (acessada em 23/10/2026) — ver docs/NORMAS_VERSOES.md
    "PT-EC": "Estrutura Conceitual (original)", "PT-200": "NBC TA 200 (R1)", "PT-210": "NBC TA 210 (R1)", "PT-220": "NBC TA 220 (R3)", "PT-230": "NBC TA 230 (R1)",
    "PT-240": "NBC TA 240 (R2)", "PT-250": "NBC TA 250", "PT-260": "NBC TA 260 (R2)", "PT-265": "NBC TA 265", "PT-300": "NBC TA 300 (R1)", "PT-315": "NBC TA 315 (R2)",
    "PT-320": "NBC TA 320 (R1)", "PT-330": "NBC TA 330 (R1)", "PT-402": "NBC TA 402", "PT-450": "NBC TA 450 (R1)", "PT-500": "NBC TA 500 (R1)", "PT-501": "NBC TA 501",
    "PT-505": "NBC TA 505", "PT-510": "NBC TA 510 (R1)", "PT-520": "NBC TA 520", "PT-530": "NBC TA 530", "PT-540": "NBC TA 540 (R2)", "PT-550": "NBC TA 550",
    "PT-560": "NBC TA 560 (R1)", "PT-570": "NBC TA 570 (R1)", "PT-580": "NBC TA 580 (R1)", "PT-600": "NBC TA 600 (R2)"}


def contagem(p):
    c = {RP: 0, PLN: 0, SIM: 0}
    for _, _, cl, _ in p["procs"]:
        c[cl] += 1
    return c


linhas_idx = []
for cod in ORDEM:
    if cod == "PT-230":
        continue
    p = todos[cod]; c = contagem(p)
    linhas_idx.append([cod, p["titulo"], VERS[cod], c[RP], c[PLN], c[SIM], f"papeis_trabalho/{cod}.md"])

h_base = hashlib.sha256(open(os.path.join(RAIZ, "base_simulada", "base_investimento_vale_sintetica.csv.gz"), "rb").read()).hexdigest()
pt230 = pt(
    "PT-230", "Documentação de auditoria — índice, convenção de códigos, referências cruzadas, controle de versões, montagem e retenção", "NBC TA 230 (R1)",
    "forma, conteúdo e extensão da documentação; montagem do arquivo final; retenção; modificações após a data do relatório",
    "Organizar a documentação do dossiê de forma que um auditor experiente, sem vínculo com o trabalho, compreenda procedimentos, evidências, conclusões e julgamentos significativos.",
    "Risco de documentação **insuficiente, não rastreável ou alterada após o prazo** (afeta todas as asserções via credibilidade do trabalho).",
    "Universo: os 27 papéis de trabalho, programas, planilhas, base sintética, código e fontes deste repositório. Critério: cada PT com os campos obrigatórios (código, título, norma, objetivo, asserções, população, procedimentos, evidências, resultados, conclusão, limitações, preparador e campo de revisão).",
    [
        ("230-1", "Índice dos papéis de trabalho com classificação dos procedimentos (abaixo).", RP, "Executado"),
        ("230-2", "Convenção: `PT-<norma>`; procedimentos `<norma>-<n>`; fontes `DF p.x`, `DFP p.x`, `FCA p.x` (ver docs/fontes.md); saídas em `saidas/` e planilha com abas nomeadas.", RP, "Executado"),
        ("230-3", "Referências cruzadas entre PTs na seção 5 de cada papel; matriz de cobertura em `docs/matriz_cobertura_NBC_TA.csv`.", RP, "Executado"),
        ("230-4", "Controle de versões: histórico Git do repositório; hash SHA-256 da base e do gabarito em `base_simulada/hashes.txt`; semente 211014396.", RP, "Executado"),
        ("230-5", "Montagem e retenção: conclusão da montagem em 25/10/2026 (entrega); retenção mínima conforme política da firma e regulamentação (a confirmar em NBC PA 01/regulamentação CVM).", PLN, "Planejado"),
    ],
    "- Referências: todos os PTs; `README.md`; `docs/`. Hash SHA-256 da base (.csv.gz): `" + h_base + "`.",
    "**Índice (contagem de procedimentos por classificação)**\n\n" + tab(["Código", "Título", "Norma/versão", "Realizado c/ evidência pública", "Planejado por falta de acesso", "Simulado", "Arquivo"], linhas_idx)
    + "\n\n**Regra de ouro:** nenhum procedimento que dependa de confirmação externa, entrevista, inspeção física ou acesso a sistemas é apresentado como realizado; todos aparecem como *Planejado por falta de acesso* ou *Simulado*.",
    "Documentação **organizada e rastreável**. A retenção e a montagem em prazo regulamentar são formais (planejadas) e não se aplicam a um trabalho acadêmico.",
    "Não há papéis reais de terceiros; os hashes só garantem integridade do material do aluno."
)
todos["PT-230"] = pt230

# gravar cada PT
for cod in ORDEM:
    with open(os.path.join(RAIZ, "papeis_trabalho", f"{cod}.md"), "w", encoding="utf-8") as f:
        f.write(render(todos[cod]))

# ---------------------------------------------------------------- matriz de cobertura
cob = []
for cod in ORDEM:
    p = todos[cod]; c = contagem(p)
    cob.append(dict(papel_de_trabalho=cod, norma_versao=VERS[cod], titulo=p["titulo"], itens_abordados=p["itens"],
                    procedimentos_total=sum(c.values()), realizado_evidencia_publica=c[RP], planejado_falta_acesso=c[PLN], simulado_didatico=c[SIM],
                    arquivo=f"papeis_trabalho/{cod}.md"))
dfc = pd.DataFrame(cob)
dfc.to_csv(os.path.join(RAIZ, "docs", "matriz_cobertura_NBC_TA.csv"), index=False, encoding="utf-8-sig")
tot = dfc[["procedimentos_total", "realizado_evidencia_publica", "planejado_falta_acesso", "simulado_didatico"]].sum()
with open(os.path.join(RAIZ, "docs", "matriz_cobertura_NBC_TA.md"), "w", encoding="utf-8") as f:
    f.write("# Matriz de cobertura — NBC TA (Estrutura Conceitual e 200 a 600) × papéis de trabalho\n\n")
    f.write("Versões conforme página do CFC (acesso em 23/10/2026) — ver `NORMAS_VERSOES.md`.\n\n")
    f.write(tab(["PT", "Norma/versão", "Título", "Procs.", "Evid. pública", "Planejado", "Simulado"],
                [[r.papel_de_trabalho, r.norma_versao, r.titulo, r.procedimentos_total, r.realizado_evidencia_publica, r.planejado_falta_acesso, r.simulado_didatico] for r in dfc.itertuples()]))
    f.write(f"\n\n**Total:** {int(tot['procedimentos_total'])} procedimentos — {int(tot['realizado_evidencia_publica'])} realizados com evidência pública, "
            f"{int(tot['planejado_falta_acesso'])} planejados por falta de acesso, {int(tot['simulado_didatico'])} simulados para fins didáticos.\n")
    f.write("\nTodas as normas da faixa **Estrutura Conceitual + NBC TA 200 a 600** da relação do CFC possuem ao menos um papel de trabalho. "
            "Nenhuma norma foi tratada apenas como 'não se aplica': estoques (NBC TA 501) e a aplicabilidade formal da NBC TA 600 têm análise justificada.\n")

# ---------------------------------------------------------------- registro de versões das normas
with open(os.path.join(RAIZ, "docs", "NORMAS_VERSOES.md"), "w", encoding="utf-8") as f:
    f.write("""# Registro da versão das normas consultadas

**Fonte:** Conselho Federal de Contabilidade — página "NBC TA de Auditoria Independente" (https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/), acessada em **23/10/2026**
(conteúdo obtido por ferramenta de leitura que devolve resumo da página; datas de publicação no DOU conforme o resumo).

""" + tab(["Norma", "Versão indicada", "Publicação (DOU/Resolução, conforme a página)", "PT"],
          [["Estrutura Conceitual", "original", "DOU 25/11/2015", "PT-EC"], ["NBC TA 200", "R1", "05/09/2016", "PT-200"], ["NBC TA 210", "R1", "05/09/2016", "PT-210"],
           ["NBC TA 220", "R3", "09/12/2021", "PT-220"], ["NBC TA 230", "R1", "05/09/2016", "PT-230"], ["NBC TA 240", "R2", "25/09/2026 (conforme a página)", "PT-240"],
           ["NBC TA 250", "original", "14/02/2019", "PT-250"], ["NBC TA 260", "R2", "04/07/2016", "PT-260"], ["NBC TA 265", "original", "Res. CFC 1.210/09", "PT-265"],
           ["NBC TA 300", "R1", "05/09/2016", "PT-300"], ["NBC TA 315", "R2", "02/09/2021", "PT-315"], ["NBC TA 320", "R1", "05/09/2016", "PT-320"],
           ["NBC TA 330", "R1", "05/09/2016", "PT-330"], ["NBC TA 402", "original", "Res. CFC 1.215/09", "PT-402"], ["NBC TA 450", "R1", "05/09/2016", "PT-450"],
           ["NBC TA 500", "R1", "05/09/2016", "PT-500"], ["NBC TA 501", "original", "Res. CFC 1.218/09", "PT-501"], ["NBC TA 505", "original", "Res. CFC 1.219/09", "PT-505"],
           ["NBC TA 510", "R1", "05/09/2016", "PT-510"], ["NBC TA 520", "original", "Res. CFC 1.221/09", "PT-520"], ["NBC TA 530", "original", "Res. CFC 1.222/09", "PT-530"],
           ["NBC TA 540", "R2", "23/10/2019", "PT-540"], ["NBC TA 550", "original", "Res. CFC 1.224/09", "PT-550"], ["NBC TA 560", "R1", "05/09/2016", "PT-560"],
           ["NBC TA 570", "R1", "25/09/2026 (conforme a página)", "PT-570"], ["NBC TA 580", "R1", "05/09/2016", "PT-580"], ["NBC TA 600", "R2", "06/12/2023", "PT-600"]]) + """

## Ressalvas importantes

1. **O texto integral das normas não foi lido nem transcrito nesta sessão.** Os papéis de trabalho aplicam a estrutura e os conceitos das NBC TA (convergentes às ISA) a partir do conhecimento geral do preparador; as citações de itens são indicativas e devem ser conferidas no texto oficial antes de qualquer uso profissional.
2. As datas "25/09/2026" para as NBC TA 240 (R2) e 570 (R1) vêm do resumo da página do CFC e são **posteriores à data-base** (31/12/2025): a vigência para o exercício de 2025 **precisa ser confirmada**. Os PT-240 e PT-570 aplicam os conceitos que não dependem de requisitos novos.
3. Ao citar "NBC TA 600 (R2)", considere que a aplicação à coligada por equivalência é interpretativa (ver PT-600).
""")

# ---------------------------------------------------------------- fontes
fontes = [
    ["F1", "Demonstrações Financeiras Bradespar 2025 (Relatório da Administração, DFs, notas, relatório do auditor, 46 p. impressas)", "Bradespar S.A.",
     "https://publish-p128342-e1259725.adobeaemcloud.com/content/dam/banco-bradesco/bradespar/staticfiles/assets/pdf/relatorios-cvm/relatorio-financeiro/Demonstrações%20Financeiras%20Bradespar%202025.pdf (publicado pelo RI da Bradespar)", "23/10/2026",
     "DF p.2–3 (estrutura dos investimentos); p.14–19 (DFs); p.20–41 (notas 1–18); p.41 (órgãos); p.42–46 (relatório do auditor)", "2025 (comparativo 2024)", "fontes/ (não versionada se houver restrição de uso)"],
    ["F2", "DFP — Demonstrações Financeiras Padronizadas 31/12/2025 (50 p.)", "Bradespar S.A. / CVM (código CVM 1872-4)",
     "https://publish-p128342-e1259725.adobeaemcloud.com/content/dam/banco-bradesco/bradespar/staticfiles/assets/pdf/relatorios-cvm/2025-itr/DFP%202025.pdf (RI da Bradespar). Consulta CVM: https://www.rad.cvm.gov.br/ENET/frmConsultaExternaCVM.aspx", "23/10/2026",
     "DFP p.21 (serviços do auditor); p.42–44 (acionistas e cadeia de controle); p.45–47 (relatório); p.48 (Conselho Fiscal); p.49–50 (declarações dos diretores)", "2025", "idem"],
    ["F3", "FCA — Formulário Cadastral 2026, versão 1 (6 p.)", "Bradespar S.A. / CVM", "https://publish-p128342-e1259725.adobeaemcloud.com/content/dam/banco-bradesco/bradespar/staticfiles/assets/pdf/relatorios-cvm/formulario-cadastral/FCA%20Versão%20Anual%20Bradespar%202026_PT.pdf (RI da Bradespar)", "23/10/2026",
     "FCA p.1 (dados gerais; sem nome anterior; ações BRAP3/BRAP4); p.4 (auditores); p.5 (escriturador)", "2026 (cadastral)", "idem"],
    ["F4", "NBC TA de Auditoria Independente (página do CFC)", "Conselho Federal de Contabilidade", "https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-ta-de-auditoria-independente/", "23/10/2026",
     "Lista de normas e revisões (resumo)", "n/a", "docs/NORMAS_VERSOES.md"],
    ["F5", "Bradespar — resultados do 2T26 (notícia)", "Eu Quero Investir (fonte **secundária**)", "https://euqueroinvestir.com/acoes/bradespar-lucro-2t26-resultados", "23/10/2026",
     "Texto integral (resumo obtido por ferramenta de leitura): lucro 2T26/1S26, caixa, recompra e remuneração da Vale", "2026 (T2)", "PT-560, PT-570 (informativo)"],
    ["F6", "Base de lotes SINTÉTICA e gabarito de erros", "Gerada pelo aluno (codigo/01_gerar_base.py)", "Repositório GitHub", "23/10/2026", "Todas as linhas", "Sintético (referência 2025)", "base_simulada/"],
    ["F7", "Planilha de cálculos (materialidade, conciliações, analíticos)", "Gerada pelo aluno (codigo/05_planilhas.py)", "Repositório GitHub", "23/10/2026", "Todas as abas", "2025", "planilhas/"],
]
cols = ["id", "documento", "emissor", "url_ou_origem", "data_acesso", "paginas_utilizadas", "exercicio", "arquivo_local"]
pd.DataFrame(fontes, columns=cols).to_csv(os.path.join(RAIZ, "fontes", "fontes.csv"), index=False, encoding="utf-8-sig")
with open(os.path.join(RAIZ, "docs", "fontes.md"), "w", encoding="utf-8") as f:
    f.write("# Registro de fontes (URL, data de acesso, documento, páginas, exercício)\n\n")
    f.write(tab(cols, fontes))
    f.write("""

## Observações

- **Mudanças de nome/ticker:** o FCA (p.1) informa *nome empresarial anterior: vazio*; as ações listadas são **BRAP3** (ON) e **BRAP4** (PN) desde 2000/2001 (FCA p.3). Não foi identificada mudança de nome ou ticker; a empresa atribuída (Bradespar S.A.) foi mantida.
- **Auditores:** PricewaterhouseCoopers (09/05/2019 a 03/05/2024) e Baker Tilly 4Partners (desde 06/05/2024) — FCA p.4.
- **Contatos:** nenhuma empresa, auditor, cliente ou fornecedor foi contatado. O acesso ao site de RI foi bloqueado por robôs; os PDFs foram baixados pelo aluno.
- **Links:** os três PDFs foram indicados pelo aluno a partir do site de RI da Bradespar (hospedagem da companhia); os arquivos baixados estão em `fontes/`.
""")

# ---------------------------------------------------------------- programas de auditoria por ciclo
prog = []


def programa(titulo, aplic, riscos, passos):
    s = f"## {titulo}\n\n**Aplicabilidade:** {aplic}\n\n**Riscos/asserções:** {riscos}\n\n"
    s += tab(["Ref.", "Procedimento", "Classificação", "PT"], passos) + "\n"
    return s


with open(os.path.join(RAIZ, "docs", "programas_de_auditoria.md"), "w", encoding="utf-8") as f:
    f.write("# Programas de auditoria por ciclo (conforme aplicáveis à Bradespar S.A. — 2025)\n\n"
            "> Preparado por: matrícula 211014396 — 23/10/2026. Revisão: ________ (sem assinatura simulada).\n\n")
    f.write(programa("1. Receitas (resultado de equivalência, JCP/dividendos e receitas financeiras)",
                     "**Aplicável.** A holding não tem receita de vendas; a 'receita' é equivalência (R$ 571.264 mil), recebimento de proventos da Vale e receitas financeiras (R$ 75.615 mil).",
                     "Ocorrência, exatidão, corte e classificação; risco de fraude presumido em receita (PT-240).",
                     [["R1", "Recalcular a equivalência com participação e resultado ajustado da Vale (A1/A2).", RP, "PT-520"],
                      ["R2", "Conciliar JCP e dividendos declarados com a movimentação do investimento e com a DFC.", RP, "PT-330, 550"],
                      ["R3", "Testar a base sintética em 100% e por MUS (recálculo pro rata, duplicidades, corte).", SIM, "PT-500, 530"],
                      ["R4", "Receitas financeiras: expectativa por saldos médios do fundo.", PLN, "PT-520 (A4)"],
                      ["R5", "Testar lançamentos manuais de fechamento no razão real.", PLN, "PT-240"]]))
    f.write("\n" + programa("2. Caixa e equivalentes de caixa",
                            "**Aplicável (imaterial)**: R$ 18.402 mil (0,23% do ativo), sendo R$ 16.756 mil em fundo administrado pelo Bradesco.",
                            "Existência, direitos, classificação (equivalente de caixa ≤ 90 dias — Nota 3c).",
                            [["C1", "Conciliar Nota 7, balanço e DFC (saldo inicial + variação = saldo final).", RP, "PT-500"],
                             ["C2", "Confirmar saldos com o administrador do fundo e extrato bancário.", PLN, "PT-505, 402"],
                             ["C3", "Testar corte (recebimentos/pagamentos de dezembro e janeiro).", PLN, "PT-560"]]))
    f.write("\n" + programa("3. Estoques",
                            "**Não aplicável (justificado):** não há conta de estoques; o objeto social é participação societária; a DVA não registra insumos de mercadorias. Análogo: existência das ações da Vale (custódia).",
                            "Não há risco de estoques; risco de existência das ações tratado no ciclo de Investimentos.",
                            [["E1", "Evidenciar a inexistência de estoques (balanço, Nota 1, DVA).", RP, "PT-501"],
                             ["E2", "Confirmar quantidade de ações com depositário/custodiante.", PLN, "PT-505"]]))
    f.write("\n" + programa("4. Imobilizado, intangível e arrendamentos",
                            "**Aplicável (imaterial):** imobilizado R$ 899 mil; intangível (direito de uso do aluguel até mar/2029) R$ 4.067 mil; passivos de arrendamento R$ 4.330 mil (362 + 3.968).",
                            "Existência, valorização/amortização, apresentação.",
                            [["I1", "Reconciliar movimentos 2024→2025 (imobilizado 1.011→899; intangível 2.306→4.067).", RP, "PT-520"],
                             ["I2", "Recalcular direito de uso e passivo (taxa, prazo) com o contrato.", PLN, "PT-330"],
                             ["I3", "Inspeção física de ativos fixos.", PLN, "—"]]))
    f.write("\n" + programa("5. Passivos (dividendos/JCP a pagar, outras obrigações, tributos, contingências)",
                            "**Aplicável.** Dividendos e JCP a pagar R$ 316.563 mil; outras obrigações R$ 30.034 mil (frações de ações — 2004); tributos R$ 391 mil; contingências possíveis R$ 2.379.000 mil.",
                            "Integridade, exatidão, corte, divulgação.",
                            [["P1", "Recalcular o passivo de dividendos/JCP pela Nota 10c: 80.000 + 257.000 × 0,85 = R$ 298.450 mil vs R$ 316.563 mil (dif. R$ 18.113 mil a investigar).", RP, "PT-250, 265"],
                             ["P2", "Testar pagamento posterior (13/03/2026) com extrato bancário.", PLN, "PT-560"],
                             ["P3", "Outras obrigações: razão auxiliar por acionista/fração; análise de prescrição/baixas.", PLN, "PT-330"],
                             ["P4", "Contingências: ler a Nota 9, obter cartas de advogados e discutir classificação.", RP, "PT-501"],
                             ["P5", "Pesquisa de passivos não registrados (leituras de atas, contratos, comunicados).", PLN, "PT-250, 560"]]))
    f.write("\n" + programa("6. Estimativas contábeis (impairment do investimento, contingências, créditos tributários não ativados)",
                            "**Aplicável.** Principais estimativas: impairment do investimento (Nota 3e), probabilidade de perda (Nota 9) e não reconhecimento de créditos tributários de R$ 355.800 mil (Nota 12c).",
                            "Valorização, integridade e divulgação; viés de gestão.",
                            [["S1", "Recalcular folga de valor de mercado e sensibilidade.", RP, "PT-540"],
                             ["S2", "Avaliar premissas críticas da Vale via auditores do componente.", PLN, "PT-600"],
                             ["S3", "Avaliar reconhecimento de créditos tributários (recuperabilidade).", PLN, "PT-540"]]))
    f.write("\n" + programa("7. Investimentos (ciclo central)",
                            "**Aplicável (91,8% do ativo).**", "Existência/direitos, valorização, integridade, apresentação (PAA).",
                            [["V1", "Roll-forward do investimento (dif. zero).", RP, "PT-330"],
                             ["V2", "Teste de 100% e amostra MUS na base sintética; comparação com gabarito.", SIM, "PT-500, 530, 450"],
                             ["V3", "Confirmação de quantidade com custodiante; trabalho do auditor da Vale.", PLN, "PT-505, 600"]]))

# ---------------------------------------------------------------- conclusão integrada
with open(os.path.join(RAIZ, "docs", "conclusao_integrada.md"), "w", encoding="utf-8") as f:
    f.write(f"""# Conclusão integrada do dossiê (riscos, procedimentos, evidências e limitações)

> **Este dossiê é um trabalho acadêmico individual. Não é um relatório de auditoria e não expressa opinião sobre as demonstrações financeiras da Bradespar S.A.** Nenhum procedimento que dependa de confirmação externa, entrevista, inspeção física ou acesso a sistemas foi realizado.

## 1. Riscos
Há **quatro riscos significativos** (PT-315): valorização/integridade do investimento na Vale (91,8% do ativo), ocorrência/exatidão da equivalência patrimonial, contingências fiscais e cíveis (R$ 2.379.000 mil não provisionados) e desconsideração de controles pela administração.

## 2. Procedimentos e evidências (resumo)
- **Com evidência pública (executados):** o roll-forward do investimento fecha (R$ 8.153.681 + 571.264 − 135.589 − 1.244.600 = R$ 7.344.756 mil); recebíveis de JCP/dividendos e DFC conciliam com a Nota 13; recálculos de reserva legal, limites, dividendo mínimo e IRRF conferem; valor patrimonial confere (0,03%); folga de valor de mercado sobre o contábil é de 60,0%.
- **Indícios a investigar (hipóteses):** equivalência acima da expectativa em R$ 42.177 mil (3,83%); receita de aplicações acima da expectativa por saldos médios; diferença de R$ 18.113 mil no passivo com acionistas; ausência de divulgação de serviços do Bradesco como partes relacionadas.
- **Simulados:** base de {n0(V['n_reg'])} lotes sintéticos com {n0(V['n_erros'])} erros inseridos; testes de 100% sinalizaram {n0(V['alertas'])} ({pct(V['alertas'] / V['n_erros'])}) e a amostra MUS ({n0(V['mus_n'])} itens) apenas 1; limite superior da amostra {brl(V['mus_uel'])} ({V['mus_ratio']:.2f}× a distorção tolerável); distorção líquida de {brl(V['efeito_liq'])} ({pct(V['efeito_liq'] / 80_000_000)} da materialidade global; abaixo da PM), mas com **padrão qualitativo** de override e falha de conciliação.
- **Planejados por falta de acesso:** confirmações (custódia, fundo, advogados, Vale), controles e TI, recebimentos posteriores, trabalho dos auditores da Vale, atas, carta de representação, razão contábil.

## 3. Conclusões possíveis
1. Com a evidência pública disponível, as DFs 2025 são **internamente consistentes** e não há sinal público de distorção relevante; **isso não equivale a uma opinião**.
2. A suficiência de evidência para a equivalência patrimonial e para as contingências **não pode ser concluída** sem os itens planejados.
3. A base sintética demonstra que **testes de 100% superam a amostragem** para erros de baixa frequência e que **erros consistentes em duas fontes** exigem totais de controle independentes.

## 4. Limitações
Dados públicos em cópia PDF; ausência de razão, originais e confirmações; base sintética sem valor probatório sobre a companhia; a reconciliação quase perfeita da base é consequência do desenho; as normas não foram lidas integralmente nesta sessão (ver `NORMAS_VERSOES.md`); a revisão (campo reservado) não foi simulada.

## 5. Declaração
O preparador (matrícula {MAT}) **não emite opinião de auditoria**. Qualquer 'conclusão' acima refere-se ao alcance dos documentos consultados.
""")

tab_err = tabela_md(V['cmp_tab'][['tipo_erro','natureza','inseridos','efeito_inserido_brl','detectados_populacao']])
# ---------------------------------------------------------------- dicionário/hipóteses da base sintética
with open(os.path.join(RAIZ, "docs", "base_sintetica_metodo_e_hipoteses.md"), "w", encoding="utf-8") as f:
    f.write(f"""# Base sintética — escolha da conta, método de geração, hipóteses e reconciliação

> **TODOS OS REGISTROS DA BASE SÃO SINTÉTICOS (FICTÍCIOS).** Os totais vêm das DFs públicas; a divisão em registros individuais é artificial.

## 1. Conta de maior materialidade do ativo
Das contas do ativo em 31/12/2025 (DF p.14), **Investimentos (Nota 8) = R$ 7.344.756 mil = 91,8% do ativo total (R$ 7.999.560 mil)**; a segunda é *Dividendos e JCP a receber* (R$ 546.640 mil; 6,8%). O investimento é também o PAA do auditor (DF p.43) e o risco central (PT-315). Portanto a base sintética representa o **razão auxiliar do investimento na Vale**.

## 2. Unidade (registro individual)
Cada linha é um **sublote de custódia** de ações ordinárias da Vale (VALE3), com quantidade, parcelas do roll-forward 2025 e atributos de lançamento (data, hora, usuário). **Hipótese A1:** a fragmentação é fictícia — a Bradespar contabiliza uma única linha de investimento; a decomposição permite exercitar amostragem e testes de população em {n0(V['n_reg'])} registros ({n0(V['n_reg'] - 300)} lotes únicos + 300 duplicidades inseridas).

## 3. Hipóteses
- **A2** — Quantidade total de 163.355.000 ações (Nota 8 informa 163.355 mil; valor exato não consta das fontes coletadas).
- **A3** — Datas de origem (01/08/2017–31/12/2024) e custodiantes (C01–C06) são fictícios.
- **A4** — Conta contábil 1.2.1.01 é fictícia.
- **A5** — Datas/horas/usuários de lançamento são fictícios (97% automáticos pelo SISTEMA; 3% manuais por U01–U08, dias úteis 08h–18h).
- **A6** — O balanço publicado é tratado como ponto de comparação; diferenças entre o razão auxiliar sintético e o balanço **não** são achados sobre a Bradespar real.
- **A7** — Cada parcela do roll-forward é alocada **pro rata** à quantidade (maior resto, em centavos), de modo que a soma dos registros limpos reproduz exatamente os totais públicos: saldo inicial R$ 8.153.681.000; equivalência R$ 571.264.000; OCI −R$ 135.589.000; JCP −R$ 566.011.000; dividendos −R$ 678.589.000; saldo final R$ 7.344.756.000.

## 4. Erros inseridos (gabarito `registro_erros_inseridos.csv`)
{tab_err}

Descrição: **E1a** equivalência com taxa errada; **E1b** erro de soma; **E2** quantidade diverge da custódia; **E3** duplicidade de lote; **E4** lançamento após 24/03/2026 (corte); **E5** lançamentos manuais suspeitos (valor redondo, fim de semana, madrugada, usuário não autorizado); **E6** quantidade ≤ 0; **E7** baixa indevida (saldo zero); **E8** conta indevida; **E9** alteração consistente em razão e custódia (não localizável por linha).

## 5. Reconciliação com o saldo contábil
{tab(['Item', 'Valor (R$)'], [[r.item, n2(r.valor_brl)] for r in V['conc'].itertuples()])}

A diferença bruta entre o razão sintético ({brl(V['soma_razao'])}) e o balanço ({brl(V['saldo_bal'])}) é de **{brl(V['dif_total'])}** e é explicada pelos erros identificados pelos testes (diferença residual por arredondamento). Em dados reais, essa explicação completa **não** seria esperada.

## 6. Reprodução
`python3 codigo/01_gerar_base.py` (semente 211014396; numpy/pandas) gera os mesmos arquivos; verifique `base_simulada/hashes.txt`. Os hashes dependem de versões compatíveis de numpy/pandas.
""")

# ---------------------------------------------------------------- texto-base do dossiê (markdown único)
with open(os.path.join(RAIZ, "dossie", "dossie_completo.md"), "w", encoding="utf-8") as f:
    for nome in ["conclusao_integrada.md"]:
        pass
    f.write("# Introdução ao dossiê\n\n")
    f.write(f"""Este dossiê reúne os **27 papéis de trabalho** (Estrutura Conceitual e NBC TA 200 a 600) para as demonstrações financeiras de **31/12/2025 da Bradespar S.A.** (CNPJ 03.847.461/0001-92; tickers BRAP3/BRAP4),
elaborados pelo aluno de matrícula **{MAT}** como trabalho individual da disciplina. A base de **{n0(V['n_reg'])} registros** é **sintética**. Cada procedimento é classificado como *{RP}*, *{PLN}* ou *{SIM}*.

**Resumo executivo.** O investimento na Vale (R$ 7.344.756 mil; 91,8% do ativo) e a equivalência (R$ 571.264 mil) concentram os riscos. Com evidência pública, as conciliações **fecham**; permanecem pendentes confirmações, controles e o trabalho dos auditores da Vale.
Na base sintética, testes de 100% identificaram {pct(V['alertas'] / V['n_erros'])} dos erros inseridos; a amostra MUS de {n0(V['mus_n'])} itens teve limite superior de erro de {V['mus_ratio']:.2f}× a distorção tolerável.

""")
    f.write("\\newpage\n\n")
    for cod in ORDEM:
        txt = open(os.path.join(RAIZ, "papeis_trabalho", f"{cod}.md"), encoding="utf-8").read()
        f.write(txt + "\n\n\\newpage\n\n")
    f.write(open(os.path.join(RAIZ, "docs", "conclusao_integrada.md"), encoding="utf-8").read() + "\n\n\\newpage\n\n")
    f.write(open(os.path.join(RAIZ, "docs", "programas_de_auditoria.md"), encoding="utf-8").read().replace("# Programas", "# Programas", 1) + "\n\n\\newpage\n\n")
    f.write(open(os.path.join(RAIZ, "docs", "matriz_cobertura_NBC_TA.md"), encoding="utf-8").read() + "\n\n\\newpage\n\n")
    f.write(open(os.path.join(RAIZ, "docs", "fontes.md"), encoding="utf-8").read() + "\n\n\\newpage\n\n")
    f.write(open(os.path.join(RAIZ, "docs", "NORMAS_VERSOES.md"), encoding="utf-8").read() + "\n\n\\newpage\n\n")
    f.write(open(os.path.join(RAIZ, "docs", "base_sintetica_metodo_e_hipoteses.md"), encoding="utf-8").read() + "\n")
print("ok:", len(ORDEM), "papéis;", int(tot["procedimentos_total"]), "procedimentos")
print(dfc[["papel_de_trabalho", "procedimentos_total", "realizado_evidencia_publica", "planejado_falta_acesso", "simulado_didatico"]].to_string(index=False))
