"""Papéis de trabalho 300, 315, 320, 330, 402, 450."""
from _comum import *
import parametros as PR

D = PR.DF


def build(V):
    P = []
    ativo = D["ativo_total"]
    mg = 80_000.0                 # materialidade global (R$ mil)
    pm = 0.7 * mg
    triv = 0.05 * mg
    mespec = 27_350.0
    pmespec = 0.7 * mespec

    # ------------------------------------------------------------------ PT-300
    P.append(pt(
        "PT-300", "Planejamento da auditoria — estratégia global, plano, cronograma e programas por ciclo", "NBC TA 300 (R1)",
        "atividades preliminares; estratégia global; plano de auditoria; natureza, época e extensão; supervisão",
        "Definir a estratégia global e o plano de auditoria das DFs de 31/12/2025 da Bradespar, o cronograma e os programas por ciclo, com base em entendimento público da entidade.",
        "Riscos que moldam o plano: concentração (91,8% do ativo em uma participação), estimativas complexas da investida (PAA), contingências de R$ 2.379.000 mil, "
        "distribuição superior ao lucro e uso de lançamentos manuais. Asserções: todas, com ênfase em valorização e integridade do investimento.",
        "Fontes: DF p.14–19, notas (p.20–41), relatório do auditor (p.42–46), FCA, DFP. Critério: abordagem predominantemente **substantiva** para o investimento e contingências, com "
        "confiança limitada em controles (a testar se acessíveis).",
        [
            ("300-1", "Atividades preliminares: rodízio, independência, termos do trabalho (PT-200, PT-210).", RP, "Executado"),
            ("300-2", "Estratégia global: natureza (substantiva + analítica), época (interino: nov–dez/2025; final: fev–mar/2026), extensão (100% para população sintética; MUS para detalhes).", SIM, "Executado (didático)"),
            ("300-3", "Plano de auditoria: matriz de riscos (PT-315), materialidade (PT-320), respostas (PT-330) e programas por ciclo (docs/programas_de_auditoria.md).", RP, "Executado"),
            ("300-4", "Cronograma (abaixo) com marcos públicos: relatório do auditor em 24/03/2026; AGO em 27/04/2026 (DFP p.48).", RP, "Executado"),
            ("300-5", "Coordenação com auditores da Vale e especialistas (PT-600).", PLN, "Planejado — sem contato"),
        ],
        "- Programas por ciclo: `docs/programas_de_auditoria.md`. Referências: PT-315, PT-320, PT-330, PT-600, PT-230 (índice).",
        "**Cronograma didático (marcos públicos em negrito)**\n\n" + tab(
            ["Fase", "Período (hipotético)", "Principais PTs", "Resp."],
            [["Planejamento e aceitação", "set–out/2025", "PT-200, 210, 220, 300, 315, 320", "Preparador"],
             ["Interino — entendimento e controles", "nov–dez/2025", "PT-240, 265, 402", "Preparador"],
             ["Final — substantivos", "fev–mar/2026", "PT-330, 500–570", "Preparador"],
             ["**Aprovação das DFs e relatório do auditor**", "**24/03/2026** (DF p.1, p.46; DFP p.47)", "PT-560, 570, 580", "—"],
             ["**AGO**", "**27/04/2026** (DFP p.48)", "—", "—"],
             ["Montagem do arquivo e conclusão do dossiê", "até 25/10/2026", "PT-230, conclusão integrada", "Preparador"]]) +
        "\n\n**Programas por ciclo** (resumo): Receitas (equivalência, JCP/dividendos, receitas financeiras) — PT-330/520/530; Caixa — PT-505/402; **Estoques — não aplicável** (justificado em PT-501); "
        "Imobilizado/Intangível — analítico e recálculo; Passivos — PT-330/550/560; Estimativas — PT-540.",
        "Plano **consistente** com os riscos identificados; a abordagem é predominantemente substantiva. O cronograma é didático, exceto pelas datas públicas.",
        "O plano é hipotético e não foi discutido com a companhia; não há orçamento nem horas reais (PT-220)."))

    # ------------------------------------------------------------------ PT-315
    inv_pct = D["investimentos"] / ativo
    P.append(pt(
        "PT-315", "Entendimento da entidade, TI e controles; matriz de riscos por conta e asserção", "NBC TA 315 (R2)",
        "entendimento da entidade e do ambiente; estrutura de relatório; ambiente de TI; controles relevantes; avaliação de risco inerente e de controle; riscos significativos",
        "Obter entendimento da Bradespar (negócio, propriedade, governança, contabilidade, TI e controles) e avaliar riscos de distorção relevante por conta e asserção, identificando riscos significativos.",
        "Ver matriz abaixo: riscos significativos = (1) valorização/integridade do investimento na Vale, (2) ocorrência/exatidão da equivalência patrimonial, (3) contingências fiscais/cíveis, "
        "(4) desconsideração de controles pela administração (presunção da NBC TA 240).",
        "Fontes: Notas 1–3, 6–18 (DF p.20–40); DFP p.42–44 (posição acionária); FCA p.1–6; Relatório da Administração (DF p.2–3, estrutura dos investimentos). Seleção: todas as contas do balanço e da DRE.",
        [
            ("315-1", "Entender o negócio: holding de participações com único investimento direto (Vale, ON, 3,60% do capital/3,83% sem tesouraria), método de equivalência (CPC 18, influência significativa).", RP, "Executado"),
            ("315-2", "Entender propriedade e governança: grupo Bradesco (Cidade de Deus Cia. Comercial 36,74%, NCF 24,87% e Fundação Bradesco 14,88% das ON — DFP p.42); Conselhos e Diretoria (DF p.41).", RP, "Executado"),
            ("315-3", "Entender critérios contábeis: Nota 3 (investimentos, provisões, tributos), sem política de derivativos (Nota 16a) e sem ativos a valor justo níveis 1–3 (Nota 15).", RP, "Executado"),
            ("315-4", "Entender o investimento: fatos da Vale em 2025 (Nota 18) — impairment de níquel de ~R$ 19,5 bi, baixas de ativos de R$ 5,6 bi, baixa de ativos fiscais diferidos de ~R$ 15,5 bi, complemento de provisão Samarco de R$ 3.379 mi; lucro atribuído R$ 13,8 bi (−56%).", RP, "Executado"),
            ("315-5", "Entender TI e controles internos relevantes (fechamento da equivalência, conciliação de dividendos, segregação).", PLN, "Planejado — sem acesso"),
            ("315-6", "Avaliar risco inerente (fatores: complexidade, subjetividade, incerteza, suscetibilidade a viés/fraude) e identificar riscos significativos (matriz).", RP, "Executado"),
            ("315-7", "Avaliar riscos na base sintética: lote como unidade, padrão de erros do desenho (PT-500/530).", SIM, "Executado"),
        ],
        "- 315-1: DF p.20 (Nota 1, 3d), p.27 (Nota 8). 315-2: DFP p.42–43; DF p.41. 315-4: DF p.35 (Nota 18). Referências: PT-240, PT-320, PT-330, PT-540, PT-550, PT-600.",
        "**Matriz de riscos de distorção relevante (R$ mil, 31/12/2025)**\n\n" + tab(
            ["Conta / divulgação", "Saldo", "% ativo", "Asserções críticas", "Risco inerente", "Fraude", "Significativo?", "Resposta"],
            [["Investimentos — Vale", n0(D["investimentos"]), pct(inv_pct), "Existência, direitos, valorização, integridade", "Alto", "Médio", "**Sim (PAA)**", "PT-330, 500, 505, 530, 540, 600"],
             ["Resultado de equivalência patrimonial", n0(D["eq_pat"]), "—", "Ocorrência, exatidão, corte", "Alto", "Alto (receita)", "**Sim (PAA)**", "PT-240, 330, 520, 600"],
             ["Dividendos e JCP a receber", n0(D["div_receber"]), pct(D["div_receber"] / ativo), "Existência, valorização, corte", "Médio", "Baixo", "Não", "PT-330 (recebimento posterior), PT-505"],
             ["Caixa e equivalentes (fundo Bradesco)", n0(D["caixa"]), pct(D["caixa"] / ativo, 2), "Existência, direitos", "Baixo", "Baixo", "Não", "PT-402, 505"],
             ["Tributos a compensar (RLP)", n0(D["rlp_tributos"]), pct(D["rlp_tributos"] / ativo), "Valorização (recuperabilidade)", "Médio", "Baixo", "Não", "PT-250, 330"],
             ["Imobilizado + Intangível + arrendamentos", "899 + 4.067 + 4.330", "0,1%", "Valorização, mensuração", "Baixo", "Baixo", "Não", "PT-520"],
             ["Dividendos e JCP a pagar", n0(D["div_jcp_pagar"]), "passivo", "Integridade, exatidão", "Médio (dif. R$ 18.113 mil)", "Médio", "Não", "PT-250, 265"],
             ["Outras obrigações (frações de ações — 2004)", n0(D["outras_obrig"]), "passivo", "Integridade, exatidão, prescrição", "Médio", "Baixo", "Não", "PT-330"],
             ["Passivos contingentes possíveis (Litel R$ 1,4 bi; autuação R$ 979 mi)", "2.379.000 (não provisionado)", "—", "Integridade, valorização, divulgação", "Alto", "Baixo", "**Sim (PAA)**", "PT-501, 540"],
             ["Despesas G&A e pessoal", n0(-D["dga"]), "—", "Ocorrência, exatidão", "Médio (+31%)", "Médio (remuneração)", "Não", "PT-520, 550"],
             ["Despesas tributárias", n0(-D["desp_trib"]), "—", "Exatidão", "Médio (+51%)", "Baixo", "Não", "PT-520"],
             ["Receitas financeiras", n0(D["rec_fin"]), "—", "Ocorrência, exatidão", "Médio", "Médio", "Não (indício PT-520 A4)", "PT-520"],
             ["Partes relacionadas (divulgação)", "—", "—", "Integridade, apresentação", "Médio", "Médio", "Não", "PT-550"],
             ["Desconsideração de controles (lançamentos manuais)", "—", "—", "Todas", "Alto (presumido)", "Alto", "**Sim (NBC TA 240)**", "PT-240"]]),
        "Identificados **quatro** riscos significativos (investimento, equivalência, contingências, desconsideração de controles). Riscos de caixa, ativos fixos e tributos são baixos/moderados "
        "pelo valor, mas mantêm resposta mínima. O entendimento de TI e controles é **lacuna** (planejado).",
        "Entendimento feito exclusivamente com documentos públicos; ausência de TI/controles; a classificação de risco é julgamento do preparador."))

    # ------------------------------------------------------------------ PT-320
    P.append(pt(
        "PT-320", "Materialidade — global, para execução e específica", "NBC TA 320 (R1)",
        "determinação da materialidade; referencial; materialidade para execução; materialidade específica; revisão durante a auditoria",
        "Determinar a materialidade global, a materialidade para execução (PM), o limite de claramente trivial e materialidades específicas, com justificativa e análise de sensibilidade.",
        "Todas as asserções no nível das DFs; materialidades específicas para itens de resultado/distribuições e remuneração de administradores (sensibilidade qualitativa).",
        "Fontes: DF p.14–15 (ativo, PL, lucro, equivalência). Cálculo: planilha `calculos_papeis_de_trabalho.xlsx` — aba `Materialidade` (fórmulas editáveis).",
        [
            ("320-1", "Escolher o referencial: ativo total (R$ 7.999.560 mil) × 1% = R$ 79.996 mil → **R$ 80.000 mil**.", RP, "Executado"),
            ("320-2", "Cruzar com PL (1% = R$ 76.478 mil) e lucro (5% = R$ 27.350 mil): lucro volátil (−54% a/a) e derivado da investida; ativo é mais estável.", RP, "Executado"),
            ("320-3", "Materialidade para execução = 70% (risco elevado: PAAs, estimativas da investida) = **R$ 56.000 mil**.", RP, "Executado"),
            ("320-4", "Claramente trivial = 5% = **R$ 4.000 mil** (itens isolados não sistemáticos).", RP, "Executado"),
            ("320-5", "Materialidade específica — resultado e distribuições: 5% × lucro = **R$ 27.350 mil** (PM específica R$ 19.145 mil).", RP, "Executado"),
            ("320-6", "Materialidade específica — remuneração de administradores: 5% × R$ 18.660 mil = **R$ 933 mil** (sensibilidade qualitativa; NBC TA 550).", RP, "Executado"),
            ("320-7", "Revisar materialidade se fatos novos (ex.: perda provável em contingência).", PLN, "Planejado"),
        ],
        "- Fórmulas: planilha, aba `Materialidade` (D4:D15). Referências cruzadas: PT-330, PT-450, PT-520 (limite), PT-530 (distorção tolerável).",
        "**Resumo (R$ mil)**\n\n" + tab(
            ["Medida", "Base", "%", "Valor"],
            [["Materialidade global", "Ativo total 7.999.560", "1%", n0(mg)], ["Materialidade para execução (PM)", "Global", "70%", n0(pm)],
             ["Claramente trivial", "Global", "5%", n0(triv)], ["Específica — resultado/distribuições", "Lucro 546.993", "5%", n0(mespec)],
             ["PM específica de resultado", "Específica", "70%", n0(pmespec)], ["Específica — remuneração de administradores", "18.660", "5%", "933"]]) +
        f"\n\n**Razoabilidade:** a materialidade global equivale a 14,6% do lucro, 1,05% do PL e 0,68% do valor de mercado da Vale (R$ 11.754.997 mil). "
        f"**Sensibilidade:** se o referencial fosse o lucro (R$ {n0(mespec)} mil, PM R$ {n0(pmespec)} mil), a distorção líquida sintética de {brl(V['efeito_liq'])} superaria a PM; "
        "por isso o PT-450 avalia a parcela que afeta resultado contra a materialidade **específica**.",
        "Materialidade global de R$ 80.000 mil e PM de R$ 56.000 mil adotadas para as DFs; materialidade específica de R$ 27.350 mil para resultado/distribuições. O julgamento é "
        "defensável por estabilidade do referencial, mas **o resultado é sensível ao referencial** (ver acima).",
        "Sem informações de usuários reais (ex.: expectativas de acionistas); sem dados históricos de erros; percentuais são práticas didáticas, não normas."))

    # ------------------------------------------------------------------ PT-330
    P.append(pt(
        "PT-330", "Respostas do auditor aos riscos avaliados — testes de controles e procedimentos substantivos", "NBC TA 330 (R1)",
        "respostas globais; procedimentos adicionais; testes de controles; procedimentos substantivos; suficiência e adequação da evidência",
        "Relacionar cada risco avaliado (PT-315) aos procedimentos de resposta, indicando o que foi **executado** (com evidência pública ou simulado) e o que ficou **planejado**.",
        "Respostas por risco significativo: investimento/equivalência (valorização, exatidão, corte), contingências (integridade, divulgação), desconsideração de controles.",
        "Fontes: DF e DFP; base sintética; planilha de cálculos. Critério: cada resposta com natureza, época e extensão e referência ao PT que contém a execução.",
        [
            ("330-1", "Roll-forward do investimento: 8.153.681 + 571.264 − 135.589 − 1.244.600 = 7.344.756 (diferença **zero**).", RP, "Executado (planilha `Concil_Investimento`)"),
            ("330-2", "Reconciliar dividendos/JCP a receber: 256.391 × (1 − 15%) + 328.708 = 546.640,35 vs 546.640 (dif. 0,35).", RP, "Executado"),
            ("330-3", "Reconciliar DFC (R$ 685.334 mil) com Nota 13: 309.620 × 0,85 + 349.881 + 72.276 = 685.334 (dif. 0).", RP, "Executado"),
            ("330-4", "Analíticos de equivalência/valor patrimonial/receitas (PT-520).", RP, "Executado"),
            ("330-5", "Detalhes sobre a base sintética: 100% dos registros (testes T0–T9) e MUS (PT-530).", SIM, "Executado"),
            ("330-6", "Teste de recebimento posterior de dividendos e JCP a receber (extratos bancários após 31/12/2025) e comunicados da Vale.", PLN, "Planejado — sem acesso aos extratos"),
            ("330-7", "Obter relatório/instruções dos auditores da Vale e avaliar resultados da auditoria do componente (PT-600).", PLN, "Planejado"),
            ("330-8", "Testes de controles (walkthrough e teste de operação) da equivalência e conciliações; autorização de lançamentos manuais.", PLN, "Planejado"),
            ("330-9", "Confirmações externas (custódia, fundo, advogados, Vale) — modelos no PT-505.", PLN, "Planejado — nada enviado"),
            ("330-10", "Teste substantivo de corte e eventos subsequentes (PT-560).", RP, "Executado (limitado a documentos públicos)"),
        ],
        "- Evidências: planilha `Concil_Investimento`, `Analiticos`; scripts 02–04; DF p.14–18, 27, 32. Referências: PT-315, PT-500, PT-505, PT-520, PT-530, PT-540, PT-560, PT-600.",
        "**Mapa risco → resposta**\n\n" + tab(
            ["Risco", "Natureza", "Época", "Extensão", "Situação"],
            [["Investimento (V, C)", "Substantiva (roll-forward, analítico, componente)", "Final", "100% do saldo", "Parcial: RP + PLN"],
             ["Equivalência (Occ/Exat/Corte)", "Substantiva (recálculo, analítico) + controle", "Interino e final", "100% + MUS na base sintética", "Parcial"],
             ["Contingências", "Leitura, confirmação com advogados", "Final", "Todos os processos > R$ 1 mi", "Leitura RP; confirmação PLN"],
             ["Override (240)", "Testes de lançamentos", "Final", "100% da base sintética", "SIM (sintético); real PLN"]]),
        "As respostas **executáveis com informação pública** foram realizadas e **fecham** (roll-forward, recebíveis, DFC). Pendem as respostas que dependem de acesso (controles, confirmações, "
        "recebimentos posteriores, auditores da Vale). A auditoria **não** poderia ser concluída sem elas.",
        "Evidência pública não substitui confirmação externa nem testes de controles; resultados da base sintética não se transferem à companhia real."))

    # ------------------------------------------------------------------ PT-402
    P.append(pt(
        "PT-402", "Organizações prestadoras de serviços", "NBC TA 402",
        "entendimento dos serviços; relevância para as DFs; relatórios tipo 1 e 2; procedimentos substantivos alternativos",
        "Identificar organizações prestadoras de serviços usadas pela Bradespar e avaliar sua relevância para o processo contábil.",
        "Riscos: existência/valorização de caixa em fundo (administrado pelo Bradesco), registro de acionistas (escriturador) e custódia das ações da Vale.",
        "Fontes: Nota 7 (1) — fundos administrados pelo Bradesco (DF p.26); FCA p.5 — escriturador Banco Bradesco S.A.; Nota 3(c) — valor de mercado do fundo pela cota informada pelo administrador (DF p.21).",
        [
            ("402-1", "Identificar prestadoras: (a) administrador do fundo (Bradesco); (b) escriturador das ações da Bradespar (Bradesco); (c) agente de custódia das ações da Vale (não divulgado).", RP, "Executado"),
            ("402-2", "Avaliar relevância: fundo = R$ 16.756 mil (0,21% do ativo) < PM; escriturador não afeta saldos financeiros; custódia da Vale afeta 91,8% do ativo → **relevante**.", RP, "Executado"),
            ("402-3", "Obter relatório tipo 2 (SOC 1/ISAE 3402) da custodiante/escriturador e confirmar controles complementares.", PLN, "Planejado — sem acesso"),
            ("402-4", "Alternativa substantiva: extrato do depositário central/custodiante e informes diários públicos do fundo (CVM).", PLN, "Planejado"),
        ],
        "- 402-1: DF p.21, p.26; FCA p.5. Referências: PT-505 (confirmações), PT-550 (partes relacionadas — o Bradesco integra o grupo controlador).",
        "Os serviços do fundo são **imateriais**; a custódia das ações da Vale é **relevante** e hoje não tem evidência pública sobre quem é o custodiante nem sobre relatórios de controle.",
        "Para o fundo, risco baixo; para a custódia da Vale, resposta planejada via confirmação e extrato do depositário. **Não aplicável por imaterialidade** apenas ao fundo e escriturador.",
        "Sem acesso a contratos, relatórios SOC ou extratos; CNPJ do fundo não divulgado."))

    # ------------------------------------------------------------------ PT-450
    ct = V["cmp_tab"]
    tab_c = tab(["Tipo", "Natureza", "Inseridos", "Efeito no saldo (R$)", "Detectados pelos testes de população", "Detectados pela amostra"],
                [[r.tipo_erro, r.natureza if isinstance(r.natureza, str) else "", n0(r.inseridos), n2(r.efeito_inserido_brl), n0(r.detectados_populacao), n0(r.detectados_amostra)]
                 for r in ct.itertuples()])
    parc_res = float(ct[ct.tipo_erro.isin(["E1a", "E5"])]["efeito_inserido_brl"].sum())
    P.append(pt(
        "PT-450", "Avaliação das distorções identificadas — mapa de distorções, quantitativo e qualitativo", "NBC TA 450 (R1)",
        "acumulação de distorções; distorções factuais, de julgamento e projetadas; reavaliação de materialidade; comunicação; correção; avaliação das não corrigidas",
        "Acumular e avaliar as distorções identificadas na **base sintética** (única fonte de distorções neste exercício didático), comparando com a materialidade e fatores qualitativos.",
        "Distorções de valor (E1a, E1b, E2, E3, E5, E7, E9), de corte (E4), de classificação (E8) e de integridade (E6) no razão auxiliar do investimento.",
        f"População: {n0(V['n_reg'])} registros sintéticos. Gabarito: `base_simulada/registro_erros_inseridos.csv` ({n0(V['n_erros'])} erros). Critério: tudo que foi identificado por teste de 100% é acumulado, mesmo individualmente abaixo do limite de trivial, porque resulta de causa sistemática.",
        [
            ("450-1", "Acumular distorções por natureza (valor, corte, classificação, integridade).", SIM, "Executado"),
            ("450-2", "Separar factuais (testes de 100%), de julgamento (nenhuma) e projetadas (MUS).", SIM, "Executado"),
            ("450-3", "Comparar o total líquido com materialidade global/PM/específica (PT-320).", SIM, "Executado"),
            ("450-4", "Avaliar fatores qualitativos: padrão de override, controles, efeito em resultado, partes relacionadas.", SIM, "Executado"),
            ("450-5", "Solicitar correção à administração e reavaliar o risco; comunicar à governança (PT-260).", PLN, "Planejado — sem contato"),
            ("450-6", "Comparar inseridos × detectados (acurácia dos testes, distorção não detectada).", SIM, "Executado (script 04)"),
        ],
        "- Gabarito e detecção: `saidas/comparacao_inserido_vs_detectado.csv`, `saidas/gabarito_vs_detectado_linha_a_linha.csv`; planilha `Mapa_Distorcoes`. Referências: PT-265, PT-320, PT-500, PT-530.",
        "**Inseridos × detectados**\n\n![Erros inseridos e detectados por tipo](../saidas/fig_inseridos_detectados.png)\n\n" + tab_c +
        f"\n\n**Efeito líquido (distorções de valor):** {brl(V['efeito_liq'])} (superavaliação bruta {brl(V['super_bruta'])}; subavaliação bruta {brl(V['sub_bruta'])}).\n\n"
        + tab(["Comparação", "Valor", "Referência"],
              [["Líquido / materialidade global (R$ 80.000.000)", pct(V["efeito_liq"] / (mg * 1000)), "< 100%"],
               ["Líquido / materialidade para execução (R$ 56.000.000)", pct(V["efeito_liq"] / (pm * 1000)), "< 100%"],
               ["Parcela que afeta resultado (E1a + E5) / materialidade específica de resultado (R$ 27.350.000)", f"{brl(parc_res)} = {pct(parc_res / (mespec * 1000))}", "< 100%"],
               ["Limite superior de erro da amostra MUS / distorção tolerável", f"{brl(V['mus_uel'])} = {V['mus_ratio']:.2f}×", "> 1 → ampliar procedimentos"]]) +
        f"\n\n**Detecção:** os testes de 100% sinalizaram {n0(V['alertas'])} de {n0(V['n_erros'])} erros inseridos (**{pct(V['alertas'] / V['n_erros'])}**); os {n0(V['n_nao_det'])} erros E9 "
        "(alteração consistente no razão e na custódia) **não** são localizáveis por linha, mas aparecem como excesso no total de controle de ações (PT-500). A amostra MUS "
        f"({n0(V['mus_n'])} itens) detectou **1** erro (efeito projetado {brl(V['mus_mle'])}), ilustrando baixo poder para erros de baixa frequência.\n\n"
        "**Fatores qualitativos:** (i) 200 lançamentos manuais com padrão de desconsideração de controles; (ii) falha sistêmica de conciliação; (iii) distorções que afetam resultado (equivalência). "
        "Esses fatores justificam correção mesmo abaixo da materialidade.",
        "Em termos **quantitativos**, as distorções líquidas ficam abaixo da materialidade global e da PM, e a parcela de resultado abaixo da materialidade específica. Em termos **qualitativos**, o "
        "padrão (override e falha de conciliação) e o limite superior da amostra acima da distorção tolerável exigem **correção, ampliação de procedimentos e comunicação**. "
        "Para a Bradespar **real**, nenhuma distorção é afirmada.",
        "Distorções são inseridas de forma deliberada e o gabarito é conhecido: as taxas de detecção refletem o desenho sintético e **não** devem ser extrapoladas para auditorias reais."))
    return P
