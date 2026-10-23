"""Papéis de trabalho 500, 501, 505, 510, 520, 530, 540, 550, 560, 570, 580, 600."""
from _comum import *
import parametros as PR

D = PR.DF


def build(V):
    P = []
    mg, pm = 80_000.0, 56_000.0
    conc = V["conc"]
    conc_md = tab(["Item da conciliação", "Valor (R$)"], [[r.item, n2(r.valor_brl)] for r in conc.itertuples()])

    # ------------------------------------------------------------------ PT-500
    P.append(pt(
        "PT-500", "Evidência de auditoria — relevância, confiabilidade, suficiência e conciliação com as DFs", "NBC TA 500 (R1)",
        "procedimentos para obter evidência; informação a ser usada como evidência; relevância e confiabilidade; suficiência e adequação",
        "Avaliar a relevância, a confiabilidade e a suficiência das evidências usadas neste dossiê, conciliar os saldos usados com as DFs e explicitar as limitações dos dados públicos e sintéticos.",
        "Todas as asserções: o risco aqui é de **evidência inadequada** (cópia em PDF sem acesso ao original; dados sintéticos sem valor probatório sobre a companhia).",
        f"Fontes: DF (46 p.), DFP (50 p.), FCA (6 p.) — arquivos em `fontes/`; base sintética ({n0(V['n_reg'])} registros). Critérios: coerência interna das DFs, rastreabilidade a página, confronto de saldos entre demonstrações.",
        [
            ("500-1", "Verificar fechamento aritmético: AC (18.402+546.640+44+42=565.128); ANC (84.710+899+4.067+7.344.756=7.434.432); Ativo = Passivo+PL (7.999.560) em 2025 e 2024 (8.606.884).", RP, "Executado"),
            ("500-2", "Conciliar DMPL (PL final 7.647.771) com balanço; DFC (caixa final 18.402) com balanço e Nota 7; DRA com DMPL (OCI −135.589).", RP, "Executado"),
            ("500-3", "Conciliar o razão auxiliar **sintético** com o saldo do Balanço (quadro abaixo).", SIM, "Executado (script 02)"),
            ("500-4", "Classificar cada evidência por confiabilidade (tabela).", RP, "Executado"),
            ("500-5", "Obter originais: arquivos da CVM/ENET, razão contábil e extratos.", PLN, "Planejado — sem acesso"),
        ],
        "- 500-1/500-2: DF p.14–19; planilha `Dados_DF`, `Concil_Investimento`. 500-3: `saidas/conciliacao_razao_balanco.csv`, aba `Conc_Razao_Balanco`. Referências: PT-505, PT-510, PT-520, PT-530.",
        "**Confiabilidade das evidências**\n\n" + tab(
            ["Evidência", "Fonte", "Natureza", "Confiabilidade", "Uso"],
            [["DFs e notas (PDF)", "Companhia/CVM (externa ao auditor, interna à entidade)", "Documento de terceiro público; cópia", "Média-alta (auditado pela BT4P)", "Roll-forwards e recálculos"],
             ["Relatório do auditor", "Terceiro (auditor)", "Original público", "Alta (autenticidade) / baixa (como prova própria)", "Contexto (PAAs)"],
             ["FCA/DFP — governança/auditores", "Companhia/CVM", "Cadastro", "Alta", "Contexto/independência"],
             ["Base de lotes", "**Sintética**", "Gerada pelo aluno", "**Sem valor probatório** sobre a Bradespar", "Demonstrar métodos"],
             ["Extrato de custodiante", "**Simulado**", "Coluna da base", "Nenhum", "Ilustrar PT-505"]]) +
        "\n\n**Conciliação do razão auxiliar sintético com o Balanço (R$)**\n\n" + conc_md,
        "As DFs **fecham** internamente em todos os testes (aritmética, DMPL, DFC, DRA). O razão auxiliar sintético **não** fecha com o Balanço antes dos erros inseridos serem identificados; "
        f"após a identificação por teste, a diferença residual é de apenas R$ {n2(float(conc.loc[conc['item'].str.contains('residual'), 'valor_brl'].iloc[0]))} (arredondamento). "
        "**Atenção ao ceticismo:** essa reconciliação quase perfeita é **propriedade do desenho** (os erros foram inseridos de modo explicável); em dados reais ela não deve ser esperada e não é, por si, evidência de controle eficaz.",
        "As evidências públicas são **relevantes**, porém **insuficientes** para suportar uma opinião: faltam originais, razão contábil, confirmações e comunicações dos auditores da Vale. "
        "Os dados sintéticos servem apenas à demonstração dos procedimentos.",
        "Dados públicos são cópias em PDF recebidas do aluno; não foi possível validar autenticidade na CVM/ENET. Dados sintéticos não são evidência sobre a companhia."))

    # ------------------------------------------------------------------ PT-501
    P.append(pt(
        "PT-501", "Itens selecionados — estoques, litígios e reclamações, informações por segmento", "NBC TA 501",
        "presença em contagem de estoques; litígios e reclamações; informações por segmento",
        "Avaliar a aplicabilidade de contagem de estoques, tratar litígios e reclamações (Nota 9) e a informação por segmento (Nota 3a).",
        "Estoques: **não aplicável** (sem saldo). Litígios: integridade, valorização e divulgação de passivos contingentes. Segmento: apresentação.",
        "Fontes: Balanço (DF p.14), Nota 3(a) (p.20), Nota 9 (p.27–28), relatório do auditor — PAA (DF p.43–44).",
        [
            ("501-1", "Estoques: Balanço não possui conta de estoques; objeto social é participação societária (Nota 1); DVA sem custo de mercadorias → **não aplicável (justificado)**.", RP, "Executado"),
            ("501-2", "Análogo à contagem: existência das ações da Vale — confirmar quantidade (163.355 mil ações ON) com custodiante/depositário (PT-505).", PLN, "Planejado"),
            ("501-3", "Litígios: ler Nota 9; identificar processos, valores, fases e classificação (possível).", RP, "Executado"),
            ("501-4", "Cartas aos assessores jurídicos (modelo no PT-505) e reunião sobre classificação de perdas.", PLN, "Planejado"),
            ("501-5", "Segmento: Nota 3(a) — holding com **único segmento**; consistente com DRE sem divisão por unidade.", RP, "Executado"),
            ("501-6", "Análise de sensibilidade: efeito de reclassificação para 'provável' sobre PL e materialidade.", RP, "Executado"),
        ],
        "- 501-1: DF p.14, p.20. 501-3: DF p.27–28. 501-6: planilha `Liquidez_Continuidade`. Referências: PT-250, PT-315, PT-540, PT-570, PT-560.",
        "**Litígios (Nota 9 b)**\n\n" + tab(
            ["Processo", "Valor", "Fase", "Classificação", "Observação"],
            [["Litel Participações S.A. × Bradespar (nº 0281248-69.2018.8.19.0001)", "R$ 1,4 bi (pedido original; corrigido por encargos legais) / reconvenção de R$ 705 mi", "TJRJ reformou a sentença (27/01/2021); REsp de ambas as partes no STJ; redistribuição em 24/02/2026", "Possível", "Decisão adversa em 2ª instância; classificação depende de parecer jurídico"],
             ["Autuação IRPJ/CSL (despesas pagas à Elétron em 2018)", "≈ R$ 979 mi (inclui multa de ofício de 75% e juros SELIC até dez/2025)", "DRJ manteve (jul/2024); CARF julgou em 26/11/2025 mantendo o mérito e cancelando a multa isolada; aguarda intimação", "Possível", "Mérito mantido no CARF; efeito potencial relevante"]]) +
        f"\n\n**Sensibilidade:** R$ 2.379.000 mil (soma dos dois processos) = 31,1% do PL, 20,2% do valor de mercado da Vale e {2379000 / mg:.1f}× a materialidade global. Uma eventual reclassificação para 'provável' "
        "exigiria provisão relevante e mudaria a conclusão de continuidade/liquidez (PT-570).",
        "Estoques **não se aplicam**. Para litígios, a classificação 'possível' é um **julgamento crítico** (há decisões adversas em instâncias superiores) e a confirmação com assessores jurídicos é indispensável (planejada). "
        "Informação por segmento consistente com holding de segmento único.",
        "Sem acesso a pareceres jurídicos, andamentos e valores atualizados; não se opina sobre a probabilidade de perda."))

    # ------------------------------------------------------------------ PT-505
    P.append(pt(
        "PT-505", "Confirmações externas — modelos, controle, diferenças e alternativas (nada foi enviado)", "NBC TA 505",
        "procedimentos de confirmação; resposta; não resposta; exceções; alternativas",
        "Preparar **modelos** de confirmação, o controle de envio/recebimento e os procedimentos alternativos, sem enviar qualquer solicitação real.",
        "Existência e direitos sobre as ações da Vale; existência do caixa/fundo; integridade e valorização das contingências; valores declarados pela Vale a receber.",
        "Itens a confirmar (saldos públicos em 31/12/2025): ações ON da Vale (163.355 mil) — custodiante/depositário; fundo de investimento (R$ 16.756 mil) e disponibilidades (R$ 1.646 mil) — Bradesco; contingências — assessores jurídicos; JCP/dividendos a receber da Vale (R$ 585.099 mil brutos; líquidos de IRRF R$ 546.640 mil).",
        [
            ("505-1", "Modelos de confirmação positiva (abaixo).", SIM, "Executado (modelos)"),
            ("505-2", "Controle de confirmações (tabela) — todas com status 'NÃO ENVIADA'.", SIM, "Executado"),
            ("505-3", "Envio e recebimento reais, tratamento de diferenças e não respostas.", PLN, "Planejado — nada enviado, por vedação do trabalho"),
            ("505-4", "Procedimentos alternativos com evidência pública: recebimentos posteriores informados pela Vale (comunicados); cotação/quantidade no extrato do depositário; Nota 13.", RP, "Executado em parte (Nota 13/Concil_Investimento)"),
        ],
        "- Modelos aplicáveis aos itens acima; base sintética: coluna `quantidade_custodia_externa` simula o extrato do custodiante (PT-500/530). Referências: PT-402, PT-501, PT-560.",
        "**Modelo (DIDÁTICO — não enviado)**\n\n"
        "> Prezados senhores, a Bradespar S.A. solicita que informem diretamente ao auditor independente, por meio de resposta ao endereço indicado, a posição em 31/12/2025 de: "
        "[ações ON VALE3 em custódia: ______] / [saldo do fundo/conta: R$ ______] / [processos em que atuam: nº, valor, fase, avaliação de risco]. Em caso de divergência, descrever. "
        "**Assinatura do respondente e data: [campos em branco]**.\n\n"
        + tab(["Ref.", "Destinatário", "Informação", "Valor registrado", "Status", "Diferença", "Alternativa"],
              [["C1", "Custodiante/depositário (não divulgado)", "Ações ON da Vale", "163.355 mil", "NÃO ENVIADA", "—", "Extrato do depositário; informes da Vale"],
               ["C2", "Bradesco (administrador do fundo)", "Fundo e disponibilidades", "R$ 18.402 mil", "NÃO ENVIADA", "—", "Informe diário público do fundo; extrato bancário"],
               ["C3", "Assessores jurídicos externos", "Processos Litel e autuação", "R$ 2.379.000 mil (não provisionado)", "NÃO ENVIADA", "—", "Leitura de peças públicas/andamentos"],
               ["C4", "Vale S.A.", "JCP/dividendos declarados", "R$ 585.099 mil a receber", "NÃO ENVIADA", "—", "Comunicados ao mercado de data de pagamento; extratos"]]),
        "Nenhuma confirmação foi enviada ou recebida. As alternativas executadas (Nota 13, DFC e Balanço) **fecham numericamente**, mas não substituem a confirmação de existência das ações e dos processos.",
        "Confirmações são **planejadas**; sem elas, a existência/direitos do investimento permanece sem evidência externa direta.",
        "Os modelos não foram revisados por assessor jurídico; os destinatários C1 e C2 não têm CNPJ/identificação pública suficientes para o envio real."))

    # ------------------------------------------------------------------ PT-510
    P.append(pt(
        "PT-510", "Trabalhos iniciais — saldos iniciais (didático)", "NBC TA 510 (R1)",
        "saldos iniciais; consistência de políticas; relatório do auditor anterior; modificações no relatório",
        "Tratar o exercício como **trabalho inicial didático** e verificar a integridade dos saldos iniciais (31/12/2024), consistência das políticas contábeis e informações sobre o auditor antecessor.",
        "Saldos iniciais: existência, integridade, valorização do investimento (R$ 8.153.681 mil) e dividendos a receber (R$ 72.276 mil); consistência de políticas.",
        "Fontes: comparativos 2024 do Balanço, DRE, DMPL e DFC (DF p.14–19); Nota 2 (consistência, p.20); FCA p.4 (auditores).",
        [
            ("510-1", "Conciliar saldos iniciais com comparativos: DMPL (saldo 31/12/2024 = 8.483.367) × Balanço 2024; DFC (caixa inicial 287.950) × Balanço 2024.", RP, "Executado — conferem"),
            ("510-2", "Roll-forward do investimento a partir do saldo inicial (PT-330-1): diferença zero.", RP, "Executado"),
            ("510-3", "Políticas contábeis: administração declara aplicação consistente (Nota 2, DF p.20).", RP, "Executado"),
            ("510-4", "Auditor antecessor: PwC até 03/05/2024; Baker Tilly 4Partners desde 06/05/2024 (FCA p.4). O relatório de 2025 é a segunda auditoria da Baker Tilly (hipótese; DFP 2024 não coletada) — o trabalho inicial é **didático**.", RP, "Executado (limitado)"),
            ("510-5", "Obter DFP/relatório do auditor de 2024 e papéis do antecessor; avaliar modificações.", PLN, "Planejado — não coletado nesta sessão"),
        ],
        "- 510-1/510-2: planilha `Concil_Investimento`; DF p.14, p.17, p.18. Referências: PT-330, PT-500.",
        "Todos os saldos iniciais conferem com os comparativos: PL 2024 8.483.367 (balanço = DMPL); caixa inicial 287.950 (balanço = DFC); investimentos 8.153.681 (balanço 2024 = base do roll-forward).",
        "Não há indício público de erro nos saldos iniciais. Conclusão limitada: sem relatório do auditor anterior não se avalia eventual modificação.",
        "O relatório de 2024 não foi coletado; a classificação como 'trabalho inicial' é artifício didático."))

    # ------------------------------------------------------------------ PT-520
    an = [
        ("A1", "Equivalência: 3,60% × resultado ajustado da Vale (R$ 13.814.281 mil)", 0.036 * 13_814_281, D["eq_pat"], "Participação sobre capital total; subestima (tesouraria da investida)"),
        ("A2", "Equivalência: 3,83% (sem tesouraria) × resultado ajustado", 0.0383 * 13_814_281, D["eq_pat"], "Mais precisa; resíduo requer participação média ponderada em 2025 (ITRs da Vale)"),
        ("A3", "Investimento: 3,60% × PL ajustado da Vale (R$ 204.083.020 mil)", 0.036 * 204_083_020, D["investimentos"], "Alta aderência"),
        ("A4", "Receita de aplicações: 13,80% × média simples do caixa", 0.138 * (18_402 + 287_950) / 2, D["rec_aplic"] if "rec_aplic" in D else 55_506, "Média simples não captura fluxo intra-anual; precisão insuficiente"),
        ("A5", "G&A: pessoal 2025 + outras despesas 2024", 26_755 + 7_823, 34_541, "Aumento explicado por pessoal"),
        ("A6", "Remuneração do pessoal-chave × limite da AGO", 19_910, 18_660, "Dentro do limite"),
        ("A7", "DFC: variação de caixa = operacional + financiamento", 670_015 - 939_563, -269_548, "Fecha"),
    ]
    lim = 19_145.0
    tab_a = tab(["ID", "Análise", "Expectativa (R$ mil)", "Registrado (R$ mil)", "Diferença", "Dif. %", "Limite (R$ 19.145 mil)", "Investigar?", "Comentário"],
                [[i, a, n0(e), n0(r), n0(r - e), pct((r - e) / r) if r else "—", "19.145", "SIM" if abs(r - e) > lim else "não", c] for i, a, e, r, c in an])
    P.append(pt(
        "PT-520", "Procedimentos analíticos substantivos — expectativas, precisão, limites e cálculos reproduzíveis", "NBC TA 520",
        "procedimentos analíticos substantivos; desenvolvimento de expectativas; limite de diferença aceitável; investigação de resultados inesperados",
        "Desenvolver expectativas independentes para equivalência, valor patrimonial, receitas financeiras e despesas, com limite de diferença aceitável, e investigar desvios.",
        "Equivalência (ocorrência/exatidão), investimento (valorização), receitas financeiras (ocorrência), despesas (exatidão), fluxo de caixa (integridade).",
        "Dados: Notas 8, 11, 13, 14, 16 e demonstrações (DF p.14–35); fórmulas na planilha `Analiticos` (editável). Limite = PM específica de resultado (R$ 19.145 mil), por ser a menor materialidade aplicável.",
        [
            ("520-1", "Definir expectativas (A1–A7), precisão e limite de investigação antes de calcular.", RP, "Executado"),
            ("520-2", "Calcular diferenças e comparar com o limite; investigar as que excedem.", RP, "Executado"),
            ("520-3", "Refinar A1→A2 com participação sem tesouraria (3,83%).", RP, "Executado — resíduo de R$ 42.177 mil permanece"),
            ("520-4", "Obter ITRs/DFP da Vale (percentual médio ponderado, equalizações, ajustes) para fechar A2 e A4.", PLN, "Planejado — não coletado"),
            ("520-5", "Analíticos de população sintética: saldo por ação constante (R$ 44,96) como expectativa para T5.", SIM, "Executado (script 02)"),
        ],
        "- Fórmulas: planilha `Analiticos` (B5:G13). Dados-fonte: `Dados_DF`. Referências: PT-265 (hipóteses H2/H4), PT-315, PT-330, PT-540.",
        "**Resultados**\n\n" + tab_a +
        "\n\n**Interpretação:** (i) o valor patrimonial **confere** (A3, 0,03%); (ii) a equivalência registrada (R$ 571.264 mil) excede a expectativa com 3,83% em R$ 42.177 mil (7,4%) — acima do limite; hipóteses: participação média "
        "ponderada superior a 3,83% ao longo de 2025 (recompras da Vale) e equalizações (Nota 8 (1)); (iii) a receita de aplicações supera a expectativa por média simples (R$ 34.368 mil) — hipótese: saldos intra-anuais elevados "
        "(recebimento de R$ 685 mi e pagamento de R$ 940 mi); (iv) demais análises conferem. **Hipóteses não são constatações.**",
        "Dois desvios (A2 e A4) excedem o limite e **permanecem em investigação** por falta de dados intra-anuais e da participação média; as demais expectativas confirmam os saldos. Com a precisão atual, "
        "A2/A4 **não** permitem reduzir procedimentos substantivos.",
        "Expectativas baseadas em percentuais divulgados e em média simples; sem dados trimestrais da investida e sem saldos diários do fundo."))

    # ------------------------------------------------------------------ PT-530
    erros_md = tab(["id_registro", "Estrato", "Saldo (R$)", "Distorção (R$)", "Teste que detectou"],
                   [[r.id_registro, r.estrato, n2(r.saldo_final_2025_brl), n2(r.distorcao_brl), r.teste_primario_detectado] for r in V["mus_erros"].itertuples()])
    ct = V["cmp_tab"]
    P.append(pt(
        "PT-530", "Amostragem em auditoria — MUS sobre a base sintética obrigatória", "NBC TA 530",
        "desenho da amostra; tamanho; seleção; execução dos procedimentos; investigação de desvios e distorções; projeção; avaliação dos resultados",
        "Aplicar amostragem por unidade monetária (MUS) à base sintética de 520.000 lotes (conta Investimentos), projetar distorções e comparar com os testes de 100% e com o gabarito de erros.",
        "Valorização, existência e exatidão dos lotes de ações da Vale (superavaliação); classificação e corte (por atributos).",
        f"População: {n0(V['n_reg'])} lotes (valor contábil de saldos positivos R$ {n2(V['mus_pop'])}); unidade: real do saldo final; método: MUS sistemática com início aleatório (semente 211014397 = matrícula + 1); "
        f"intervalo R$ {n2(V['mus_J'])}; início R$ {n2(V['mus_inicio'])}; amostra {n0(V['mus_n'])} itens; nenhum item ≥ intervalo (estrato de topo vazio). Saldos zero/negativos não podem ser selecionados por MUS e foram cobertos pelos testes de 100%.",
        [
            ("530-1", "Definir parâmetros: confiança 95%, distorção tolerável = PM R$ 56.000.000, distorção esperada R$ 5.000.000 (hipótese), fator de expansão 1,6.", SIM, "Executado"),
            ("530-2", f"Tamanho: n = VC × 2,9957 ÷ (56.000.000 − 5.000.000 × 1,6) = {n0(V['mus_n'])}.", SIM, "Executado"),
            ("530-3", "Selecionar por MUS sistemática (script 03) — lista em `planilhas/amostra_MUS.csv`.", SIM, "Executado"),
            ("530-4", "Executar procedimentos de detalhe por item (recálculo, quantidade × custódia, duplicidade, corte, conta).", SIM, "Executado"),
            ("530-5", "Projetar a distorção (Stringer 95%) e comparar com a distorção tolerável.", SIM, "Executado"),
            ("530-6", "Comparar com testes de 100% e gabarito: risco de amostragem.", SIM, "Executado (script 04)"),
        ],
        "- Reprodução: `python3 codigo/03_amostragem_mus.py`; saídas `saidas/mus_resumo.csv`, `saidas/mus_erros_na_amostra.csv`; planilha `Parametros_MUS`. Referências: PT-320, PT-450, PT-500.",
        "**Parâmetros e resultados (R$)**\n\n" + tab(["Item", "Valor"], [[k, str(v)] for k, v in V["mus"].items()]) +
        "\n\n**Erros encontrados na amostra**\n\n" + erros_md +
        f"\n\n**Projeção:** distorção mais provável {brl(V['mus_mle'])}; limite superior de erro (Stringer, 95%) **{brl(V['mus_uel'])}** = {V['mus_ratio']:.2f}× a distorção tolerável → "
        f"**{V['mus_concl']}**. A população tem {n0(V['n_erros'])} erros inseridos ({n0(V['n_erros'] - V['n_nao_det'])} detectáveis por linha); a amostra de {n0(V['mus_n'])} itens selecionou apenas "
        f"{n0(int(V['cmp']['erros_na_amostra']))} deles e detectou {n0(int(V['cmp']['erros_detectados_pela_amostra']))}: **risco de amostragem elevado** para erros de baixa frequência. Os testes de 100% revelam {brl(V['efeito_liq'])} de distorção líquida, "
        f"contra {brl(V['mus_mle'])} projetados pela amostra (subestimação de {brl(V['efeito_liq'] - V['mus_mle'])}).",
        "A amostra **não apoia a aceitação** sem ajustes (UEL > TM), e sua projeção subestima a distorção real conhecida. A conclusão correta para o auditor é **ampliar a amostra ou usar testes de 100%** (o que "
        "a automação permite), com correção das distorções identificadas. Isto confirma que amostra isolada tem baixo poder para detectar fraude/erros esparsos.",
        "O gabarito só existe em dados sintéticos; em dados reais, a distorção verdadeira é desconhecida. O fator de expansão e a distorção esperada são hipóteses; o desvio tolerável por atributos não foi calculado."))

    # ------------------------------------------------------------------ PT-540
    mk, bk = 11_754_997.0, 7_344_756.0
    shares = 163_355.0
    px = mk / shares
    sens = tab(["Choque no preço da Vale", "Valor de mercado (R$ mil)", "Folga sobre o valor contábil (R$ mil)", "Folga %"],
               [[f"{c:+.0%}", n0(mk * (1 + c)), n0(mk * (1 + c) - bk), pct((mk * (1 + c) - bk) / bk)] for c in (0, -0.1, -0.2, -0.3, -0.375, -0.4)])
    P.append(pt(
        "PT-540", "Estimativas contábeis — redução ao valor recuperável (impairment) do investimento na Vale", "NBC TA 540 (R2)",
        "entendimento do processo; fatores de risco inerente (complexidade, subjetividade, incerteza); métodos, dados e premissas; viés; estimativa pontual × intervalo; divulgações",
        "Auditar **uma** estimativa selecionada: avaliação de indícios de impairment do investimento na Vale (Nota 3(e)), comparando o valor contábil com o valor de mercado da participação, com sensibilidade e avaliação de viés. "
        "Contingências (PT-501) e equivalência (PT-600) são tratadas como estimativas adicionais da investida.",
        "Valorização do investimento (R$ 7.344.756 mil); apresentação/divulgação (Nota 8 (3)). Fatores: **complexidade** média (valor de mercado observável), **subjetividade** baixa (preço de mercado), "
        "**incerteza** moderada (volatilidade das commodities, litígios e provisões da Vale).",
        "Dados: valor de mercado da participação em 30/12/2025: R$ 11.754.997 mil (2024: R$ 8.910.993 mil) — Nota 8 (3), DF p.27; ações: 163.355 mil (Nota 8); valor contábil: R$ 7.344.756 mil. "
        "Método da administração: avalia 'ao final de cada exercício' se há evidências de deterioração; **não houve impairment em 2025 e 2024** (Nota 3(e), DF p.21).",
        [
            ("540-1", "Entender o processo e a política: Nota 3(e) e Nota 4 (estimativas e julgamentos).", RP, "Executado"),
            ("540-2", f"Recalcular: valor de mercado ÷ ações = R$ {n2(px)} por ação; folga = 11.754.997 − 7.344.756 = R$ {n0(mk - bk)} mil ({pct((mk - bk) / bk)} sobre o valor contábil).", RP, "Executado"),
            ("540-3", "Comparar com 2024: folga de R$ 757.312 mil (9,3%) — a folga **cresceu** (indício contra viés de manutenção).", RP, "Executado"),
            ("540-4", "Sensibilidade: queda de 37,5% no preço zera a folga (tabela).", RP, "Executado"),
            ("540-5", "Avaliar viés: a administração não reconheceu impairment em ano de forte queda do lucro da Vale (−56%), mas o preço de mercado supera o contábil.", RP, "Executado"),
            ("540-6", "Obter cotação oficial B3 de 30/12/2025 e confirmar quantidade de ações; considerar custo de alienação e liquidez de bloco.", PLN, "Planejado — não coletado"),
            ("540-7", "Avaliar premissas críticas da Vale (barragens, provisões fiscais, impairment de níquel) via auditores da Vale (PT-600).", PLN, "Planejado"),
        ],
        "- Planilha `Concil_Investimento` (B38:B39). Referências: PT-315, PT-501, PT-570, PT-600.",
        "**Sensibilidade do valor recuperável (R$ mil)**\n\n" + sens +
        f"\n\nO preço de mercado implícito é R$ {n2(px)} por ação. O valor de mercado é **observável** (nível 1), mas a Nota 8 (3) não detalha cotação nem custos de alienação; "
        "a medida de recuperabilidade segue CPC 01 (maior entre valor justo líquido de despesas e valor em uso) — **o valor em uso não foi estimado**.",
        "A estimativa da administração (**ausência de impairment**) é **razoável** com a evidência pública: o valor de mercado supera o contábil em 60,0%, com folga crescente vs. 2024. A conclusão depende da confirmação "
        "da cotação e da quantidade (planejadas). Viés: não identificado.",
        "Valor de mercado vem da própria Nota; sem preço oficial, sem custo de alienação, sem análise de bloco/liquidez e sem valor em uso."))

    # ------------------------------------------------------------------ PT-550
    P.append(pt(
        "PT-550", "Partes relacionadas — identificação, transações, divulgação e remuneração", "NBC TA 550",
        "identificação de partes relacionadas; avaliação de riscos; transações significativas fora do curso normal; divulgações; representações",
        "Identificar partes relacionadas e verificar a completude e a exatidão da Nota 13 com evidência pública.",
        "Integridade e apresentação das divulgações; ocorrência/exatidão de JCP e dividendos da Vale; remuneração de administradores (risco de override e de limite da AGO).",
        "Fontes: Nota 13 (DF p.32–33); DFP p.42–44 (acionistas e cadeia de controle); FCA p.5 (escriturador Bradesco); Nota 7 (1) (fundo administrado pelo Bradesco).",
        [
            ("550-1", "Listar partes relacionadas: Vale (coligada); grupo controlador (Cidade de Deus Cia. Comercial, NCF Participações, Fundação Bradesco); Banco Bradesco (administrador do fundo e escriturador); administradores.", RP, "Executado"),
            ("550-2", "Recalcular Nota 13 I: JCP recebidos 309.620 + a receber 256.391; dividendos recebidos 349.881 + a receber 328.708 = R$ 1.244.600 mil (= movimentação do investimento).", RP, "Executado"),
            ("550-3", "Remuneração: R$ 18.660 mil em 2025 (R$ 15.000 mil em 2024; +24,4%) ≤ limite AGO R$ 19.910 mil (19.391 + 519 previdência).", RP, "Executado"),
            ("550-4", "**Completude:** não há divulgação de transações com o Banco Bradesco (administração de fundo, escrituração) — verificar se há remuneração/tarifa e se são imateriais.", RP, "Executado (indício)"),
            ("550-5", "Indagar a administração sobre transações com controladores e partes relacionadas fora do curso normal.", PLN, "Planejado — sem contato"),
            ("550-6", "Obter lista de partes relacionadas da administração e comparar com a do auditor.", PLN, "Planejado"),
        ],
        "- 550-2: Nota 13 (DF p.32); planilha `Concil_Investimento`. 550-3: Nota 13 II; planilha `Analiticos` A6; materialidade específica R$ 933 mil (PT-320). Referências: PT-402, PT-265 (H3), PT-315.",
        "A cadeia de controle (DFP p.42–43) mostra que os três maiores acionistas ON detêm 76,5% das ações ordinárias, o que confirma o **grupo Bradesco** como controlador. A movimentação de R$ 1.244.600 mil "
        "(JCP + dividendos declarados pela Vale) coincide com a variação do investimento e com a Nota 13. A remuneração fica dentro do limite aprovado, mas **cresce 24,4%** (pessoal +44,9%).",
        "Exatidão dos valores com a Vale **confirmada** por conciliação; remuneração **dentro do limite**; **indício de omissão** de divulgação de serviços do Bradesco (hipótese H3), a esclarecer.",
        "Sem lista de partes relacionadas da administração; sem contratos; valores de tarifas desconhecidos."))

    # ------------------------------------------------------------------ PT-560
    P.append(pt(
        "PT-560", "Eventos subsequentes — data de corte, publicações posteriores, ajuste × divulgação", "NBC TA 560 (R1)",
        "eventos até a data do relatório; fatos após a data do relatório e antes da emissão; fatos após a emissão; ajuste × divulgação",
        "Identificar eventos entre 31/12/2025 e a data do relatório (24/03/2026) e fatos posteriores publicados, classificando-os em ajustáveis ou de divulgação.",
        "Corte, integridade de passivos e divulgação.",
        "Fontes: Nota 17 (DF p.34); Nota 9 (p.27–28); Nota 10c (p.30); DFP p.48 (AGO em 27/04/2026); notícia sobre os resultados do 2T26 (13/08/2026) — fonte **secundária** (https://euqueroinvestir.com/acoes/bradespar-lucro-2t26-resultados, acessada em 23/10/2026).",
        [
            ("560-1", "Data de corte: DFs autorizadas pelo Conselho e relatório do auditor em **24/03/2026** (DF p.20, p.46).", RP, "Executado"),
            ("560-2", "Fato (1) — 12/03/2026: Vale cancelou 99.847.816 ações em tesouraria sem reduzir capital (Nota 17) → **não ajustável**; aumenta o percentual da Bradespar sobre o capital.", RP, "Executado"),
            ("560-3", "Fato (2) — 13/03/2026: pagamento de dividendos R$ 80.000 mil e JCP R$ 257.000 mil (bruto) (Nota 10c) → liquida o passivo (R$ 298.450 mil líquido de IRRF) — **não ajustável**; confirma o passivo.", RP, "Executado"),
            ("560-4", "Fato (3) — 24/02/2026: redistribuição dos recursos da Litel no STJ (Nota 9) e aguarda-se intimação do CARF → **divulgação**, sem ajuste.", RP, "Executado"),
            ("560-5", "Fato após o relatório (fonte secundária, 13/08/2026): lucro 2T26 R$ 252,3 mi, 1S26 R$ 805,8 mi; caixa de R$ 254,5 mi em 30/06/2026; sem dívida financeira; Vale anunciou recompra de até 100 milhões de ações (30/07/2026) e remuneração de US$ 1,7 bi a pagar em 02/09/2026.", RP, "Informativo (não é evento subsequente da auditoria de 2025)"),
            ("560-6", "Testar corte na base sintética: 150 lançamentos de equivalência de 2025 lançados após 24/03/2026 (E4/T6).", SIM, "Executado"),
            ("560-7", "Indagar a administração; ler atas até a data do relatório; testar recebimentos após o fechamento (extratos).", PLN, "Planejado — sem acesso"),
        ],
        "- 560-2/560-3: DF p.30, p.34. 560-5: fonte secundária (ver URL). 560-6: `saidas/excecoes_populacao.csv` (teste T6). Referências: PT-501, PT-570, PT-580.",
        "**Classificação**\n\n" + tab(["Evento", "Data", "Tipo", "Tratamento"],
                                    [["Cancelamento de ações em tesouraria da Vale", "12/03/2026", "Não ajustável", "Divulgado (Nota 17)"],
                                     ["Pagamento de dividendos/JCP declarados em dez/2025", "13/03/2026", "Não ajustável (liquidação)", "Confirma passivo"],
                                     ["Redistribuição Litel no STJ; CARF aguardando intimação", "24/02/2026 / pendente", "Divulgação", "Nota 9"],
                                     ["Resultados do 2T26 / recompra e remuneração da Vale", "13/08/2026 / 30/07/2026", "Pós-relatório (informativo)", "Sem tratamento nas DFs 2025"]]),
        "Nenhum evento **ajustável** foi identificado com evidência pública; os eventos de divulgação constam das notas. A análise é limitada à data do relatório e a fontes públicas.",
        "Dentro da data de corte, não há indícios de ajustes; **indagações e leitura de atas permanecem planejadas**.",
        "Fonte secundária (notícia) não foi validada contra o comunicado oficial; a análise não cobre atas ou comunicações privadas."))

    # ------------------------------------------------------------------ PT-570
    stress_cov = (1_244_600 / 2) / (-D["dga"] - D["desp_trib"])
    P.append(pt(
        "PT-570", "Continuidade operacional — liquidez, dívida, covenants, fluxos de caixa e eventos adversos", "NBC TA 570 (R1 — publicação indicada em 25/09/2026; vigência a confirmar)",
        "avaliação da administração; período de pelo menos 12 meses; eventos ou condições; fluxos de caixa; planos de mitigação; incerteza relevante",
        "Avaliar se há eventos ou condições que lancem dúvida significativa sobre a continuidade, com indicadores de liquidez, dependência de dividendos da Vale, contingências e eventos posteriores.",
        "Apresentação/divulgação (base de continuidade). Fatores: dependência de um único pagador (Vale), consumo de caixa em 2025 (−R$ 269.548 mil), contingências possíveis de R$ 2.379.000 mil.",
        "Fontes: Balanço e DFC (DF p.14, 18); Nota 6 (risco de liquidez, p.25–26); Notas 9 e 14 (p.27–28, 33); planilha `Liquidez_Continuidade`; fonte secundária 2T26 (PT-560).",
        [
            ("570-1", "Indicadores: liquidez corrente 1,62 (2024: 2,97); caixa/PC 0,05 (2024: 2,37); (caixa + recebíveis)/dividendos a pagar 1,78; caixa operacional/distribuições 0,71.", RP, "Executado"),
            ("570-2", "Dívida e covenants: **sem dívida financeira**; passivos financeiros = outras obrigações (R$ 25.120 mil) e arrendamentos (R$ 4.330 mil); logo, sem covenants financeiros a testar.", RP, "Executado"),
            ("570-3", "Fluxo de caixa: operacional R$ 670.015 mil vs distribuições pagas R$ 939.563 mil → caixa caiu de R$ 287.950 para R$ 18.402 mil.", RP, "Executado"),
            ("570-4", f"Teste de estresse: se a Vale reduzisse proventos em 50% (R$ 622.300 mil), a cobertura das despesas fixas (G&A + tributárias R$ 99.356 mil) seria {stress_cov:.1f}×.", RP, "Executado (cálculo)"),
            ("570-5", "Contingências: R$ 2.379.000 mil (31,1% do PL; 129× o caixa); capacidade, em tese, via venda de ações da Vale (valor de mercado R$ 11,75 bi).", RP, "Executado"),
            ("570-6", "Eventos posteriores (fonte secundária): caixa de R$ 254,5 mi em 30/06/2026 e ausência de dívida; recompra/remuneração da Vale.", RP, "Informativo"),
            ("570-7", "Obter plano de fluxo de caixa de 12 meses e avaliação formal da administração.", PLN, "Planejado — sem acesso"),
        ],
        "- 570-1..570-5: planilha `Liquidez_Continuidade`. Referências: PT-501, PT-540, PT-560.",
        "A entidade **não tem dívida**, tem recebíveis da Vale (R$ 546.640 mil) superiores ao passivo com acionistas (R$ 316.563 mil) e um ativo líquido (participação com valor de mercado de R$ 11,75 bi). "
        "O ponto de atenção é a **dependência de dividendos** e o **consumo de caixa** em 2025, além das contingências que, se se tornarem prováveis, exigiriam venda de ativos ou captação.",
        "Com a evidência pública, **não há incerteza relevante** sobre a continuidade: relatório do auditor sem parágrafo específico e indicadores favoráveis. A conclusão é **limitada** (sem projeção da administração).",
        "Cálculo de estresse é ilustrativo; dependência de fonte secundária para 2026; sem avaliação formal da administração."))

    # ------------------------------------------------------------------ PT-580
    P.append(pt(
        "PT-580", "Representações formais — carta de representação didática", "NBC TA 580 (R1)",
        "representações da administração; responsabilidades; outras representações; data e assinatura; dúvidas sobre confiabilidade",
        "Preparar a **minuta didática** de carta de representação e explicar por que ela não substitui outra evidência.",
        "Responsabilidade pelas DFs, integridade das informações, partes relacionadas, eventos subsequentes, litígios, fraude, continuidade.",
        "Fontes: declarações dos diretores (DFP p.49–50), que são declarações regulatórias distintas da carta do auditor.",
        [
            ("580-1", "Minuta de carta de representação (abaixo).", SIM, "Executado"),
            ("580-2", "Avaliar as declarações dos diretores (DFP p.49–50): concordam com o relatório e com as DFs; **não** cobrem fraude, partes relacionadas nem eventos subsequentes.", RP, "Executado"),
            ("580-3", "Obter a carta assinada, datada no mesmo dia do relatório.", PLN, "Planejado — sem acesso"),
        ],
        "- 580-2: DFP p.49–50. Referências: PT-210, PT-240, PT-450, PT-560.",
        "**Minuta (DIDÁTICA — não enviada; assinaturas reservadas)**\n\n"
        "> À [Auditor], referente à auditoria das DFs de 31/12/2025. Confirmamos, conforme nosso conhecimento: (1) cumprimos nossas responsabilidades pela elaboração das DFs conforme CPC/IFRS; "
        "(2) fornecemos todas as informações e acesso; (3) todas as transações constam dos registros; (4) divulgamos todas as partes relacionadas e transações; (5) não temos conhecimento de fraude ou suspeita; "
        "(6) todas as contingências e descumprimentos foram divulgados; (7) eventos subsequentes foram divulgados; (8) as distorções não corrigidas listadas (anexo) são imateriais; (9) a base contábil de continuidade é adequada. "
        "**[Assinatura/data: reservadas]**.\n\n**Por que não substitui outras evidências:** a representação é evidência de **menor confiabilidade** (da parte interessada); não substitui confirmações, recálculos ou testes (NBC TA 580).",
        "Minuta elaborada; as declarações dos diretores existentes são regulatórias e **não** equivalem à carta de representação do auditor.",
        "Representações reais são planejadas; a minuta não foi submetida à administração.",
        ))

    # ------------------------------------------------------------------ PT-600
    comp_mat = 0.5 * pm
    P.append(pt(
        "PT-600", "Auditorias de grupos — Vale como componente (coligada), materialidade e suficiência do trabalho", "NBC TA 600 (R2)",
        "entendimento do grupo e do componente; materialidade do componente; instruções; comunicação com o auditor do componente; suficiência da evidência",
        "A Bradespar **não possui controladas** (Nota 1: participação direta na Vale), portanto não elabora demonstrações consolidadas; porém o relatório do auditor descreve que "
        "'planejamos e executamos a auditoria do grupo' e que comunicou instruções aos auditores da Vale (DF p.43, 45). Este PT trata a Vale como **componente** (coligada) para fins didáticos.",
        "Valorização/integridade/ocorrência do resultado de equivalência dependem de estimativas da Vale (provisão de descaracterização de barragens; contingências fiscais; impairment de níquel no Canadá).",
        "Fontes: Nota 1 e 8 (DF p.20, p.27); Nota 18 (p.35–40); PAA (p.43); responsabilidades (p.45). Participação: 3,60% do capital; 3,83% sem tesouraria.",
        [
            ("600-1", "Avaliar aplicabilidade: sem controladas/consolidação, a NBC TA 600 (R2) aplica-se **por analogia** à investida avaliada por equivalência; o auditor da Bradespar afirma ter aplicado enfoque de auditoria de grupo.", RP, "Executado"),
            ("600-2", "Identificar o componente (Vale), seus riscos (Nota 18; PAA) e sua significância: 91,8% do ativo e 104% do lucro (571.264 ÷ 546.993).", RP, "Executado"),
            ("600-3", f"Materialidade do componente (didática): {pct(0.5)} da PM = R$ {n0(comp_mat)} mil na participação da Bradespar, ou R$ {n0(comp_mat / 0.0383)} mil no nível de 100% da Vale (≈ R$ 731 mi; 5,3% do lucro atribuído da Vale).", SIM, "Executado"),
            ("600-4", "Instruções ao auditor do componente e recepção das comunicações (riscos, escopo, resultados, deficiências).", PLN, "Planejado — não contatar"),
            ("600-5", "Avaliar competência/independência do auditor da Vale e suficiência do trabalho (revisar papéis, quando permitido).", PLN, "Planejado"),
            ("600-6", "Procedimentos adicionais da equipe do grupo: recalcular equivalência com DFs auditadas da Vale (disponíveis na CVM) e ajustes de equalização.", PLN, "Planejado — DFs da Vale não coletadas"),
        ],
        "- 600-1..600-2: DF p.20, 27, 35, 43, 45. Referências: PT-315, PT-320, PT-520 (A1/A2), PT-540.",
        "O auditor da Vale **não é identificado** nas fontes coletadas. A Bradespar não controla a Vale e não pode dirigir o trabalho do auditor da investida; portanto, a evidência sobre as estimativas "
        "da Vale deve ser obtida por **comunicação e leitura** (como afirma o PAA), e a Bradespar fica dependente do trabalho alheio.",
        "O componente é **significativo** em todas as dimensões. Sem acesso às comunicações e às DFs auditadas da Vale, a suficiência de evidência para a equivalência **não pode ser concluída** — "
        "o que é consistente com o status 'planejado'.",
        "Aplicabilidade formal da NBC TA 600 (R2) a coligadas por equivalência é interpretativa; sem informações do auditor da Vale."))
    return P
