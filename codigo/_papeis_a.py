"""Papéis de trabalho EC, 200, 210, 220, 240, 250, 260, 265 (230 é montado no script principal por depender do índice)."""
from _comum import *


def t(V, nome, col="registros_alertados"):
    return V["testes"].loc[V["testes"]["teste"] == nome, col].iloc[0]


def build(V):
    P = []

    # ------------------------------------------------------------------ PT-EC
    P.append(pt(
        "PT-EC", "Estrutura Conceitual — trabalho de asseguração: objeto, critérios, usuários e nível de segurança",
        "NBC TA — Estrutura Conceitual para Trabalhos de Asseguração (versão original, DOU 25/11/2015 — ver NORMAS_VERSOES.md)",
        "elementos do trabalho de asseguração (relação entre três partes, objeto, critérios, evidência, relatório); asseguração razoável × limitada",
        "Identificar, a partir do relatório do auditor independente de 24/03/2026 e das notas explicativas, os elementos do trabalho de "
        "asseguração realizado sobre as demonstrações financeiras (DFs) da Bradespar S.A. de 31/12/2025 e diferenciar a **auditoria** de outros "
        "trabalhos de asseguração, para delimitar o que este dossiê pode (e não pode) concluir.",
        "Risco de **conclusão inadequada para o nível de segurança**: apresentar como 'auditoria' um trabalho de procedimentos limitados, ou "
        "supor segurança razoável sem evidência suficiente. Asseguração aplica-se à informação sobre o objeto (as DFs) como um todo.",
        "Fontes: Relatório do auditor independente (DF p.42–46; DFP p.45–47); Nota 2 — critérios (DF p.20); Parecer do Conselho Fiscal (DFP p.48); "
        "Declarações dos diretores (DFP p.49–50). Seleção: documentos públicos entregues pelo aluno e protocolados na CVM (arquivos em `fontes/`).",
        [
            ("EC-1", "Identificar as três partes: auditor (Baker Tilly 4Partners Auditores Independentes), parte responsável (administração/Conselho de "
                     "Administração) e usuários previstos (acionistas, mercado, CVM).", RP, "Executado"),
            ("EC-2", "Identificar o objeto: DFs individuais de 31/12/2025 (balanço, DRE, DRA, DMPL, DFC, notas) e DVA como informação suplementar.", RP, "Executado"),
            ("EC-3", "Identificar critérios: práticas contábeis adotadas no Brasil (CPC/Res. CVM 72) e IFRS Accounting Standards (Nota 2).", RP, "Executado"),
            ("EC-4", "Identificar nível de segurança: segurança razoável (alto nível, não garantia) — relatório de auditoria com opinião sem ressalvas.", RP, "Executado"),
            ("EC-5", "Distinguir auditoria de: revisão de informações trimestrais (limitada), asseguração diferente de auditoria/revisão (ex.: dados de "
                     "sustentabilidade) e procedimentos previamente acordados (sem asseguração).", RP, "Executado (análise conceitual)"),
            ("EC-6", "Confirmar que o escopo do **dossiê do aluno** é de trabalho acadêmico: não emite relatório nem expressa opinião.", SIM, "Executado"),
        ],
        "- Evidência EC-1..EC-4: relatório do auditor (DF p.42: 'Opinião'; p.42: 'Base para opinião'; p.45: 'Responsabilidades do auditor').\n"
        "- Evidência EC-3: Nota 2 (DF p.20). Evidência complementar: Conselho Fiscal e diretores (DFP p.48–50).\n"
        "- Referências cruzadas: PT-200 (objetivos do auditor), PT-210 (termos do trabalho), PT-500 (evidência), PT-580 (representações).",
        "**Quadro comparativo** (preenchido pelo preparador):\n\n" + tab(
            ["Elemento", "Auditoria das DFs (caso Bradespar)", "Revisão de ITR", "Asseguração (ex.: sustentabilidade)", "Dossiê do aluno"],
            [["Partes", "Auditor × administração × usuários", "Idem", "Idem", "Aluno × (nenhuma parte real)"],
             ["Objeto", "DFs anuais 31/12/2025", "Informações trimestrais", "Informação não financeira", "Dados públicos + base sintética"],
             ["Critérios", "CPC / IFRS Accounting Standards", "Idem", "Critérios específicos do tema", "NBC TA (estudo)"],
             ["Nível", "Razoável (positivo)", "Limitada (negativa)", "Razoável ou limitada", "Nenhum (sem opinião)"],
             ["Evidência", "Suficiente e apropriada (NBC TA 500)", "Indagação e analíticos", "Conforme o trabalho", "Pública/simulada (PT-500)"],
             ["Produto", "Relatório com opinião (DF p.42)", "Relatório de revisão", "Relatório de asseguração", "Dossiê e conclusão integrada (sem opinião)"]]),
        "O relatório de 24/03/2026 contém os cinco elementos da Estrutura Conceitual e indica segurança **razoável**. O dossiê do aluno **não** é trabalho de "
        "asseguração: reproduz o raciocínio e as conclusões parciais com evidência pública e dados sintéticos, sem emitir opinião sobre as DFs.",
        "Não foi acessada a carta de contratação real nem a documentação do auditor; os elementos são inferidos do relatório publicado. O texto integral da "
        "norma não foi transcrito (ver NORMAS_VERSOES.md)."))

    # ------------------------------------------------------------------ PT-200
    P.append(pt(
        "PT-200", "Objetivos gerais, ética, independência, ceticismo, julgamento e risco de auditoria",
        "NBC TA 200 (R1)", "objetivos gerais; requisitos éticos; ceticismo e julgamento profissionais; segurança razoável; risco de auditoria",
        "Documentar como o preparador aplica ceticismo profissional e julgamento ao caso Bradespar, avaliar sinais públicos de independência do auditor "
        "e explicitar o modelo de risco de auditoria (RA = RDR × RD) usado no planejamento.",
        "Risco de **viés de confirmação** (aceitar o relatório publicado como prova), de **independência** (rodízio, serviços não auditoria) e de "
        "**subestimar o risco de detecção** em área de estimativas complexas (equivalência patrimonial da Vale). Asserções afetadas: todas, no nível das DFs.",
        "Fontes: Relatório do auditor (DF p.42, 45); Serviços não relacionados à auditoria (DFP p.21 — Res. CVM 162/22); FCA seção 4 (FCA p.4) — histórico de auditores. "
        "Critério: leitura integral dos trechos sobre independência e confronto com datas do FCA.",
        [
            ("200-1", "Ler a declaração de independência e de ética do auditor (Código de Ética Profissional do Contador; entidades de interesse público).", RP, "Executado"),
            ("200-2", "Verificar serviços não relacionados à auditoria em 2025: a Bradespar declara não ter contratado nenhum (DFP p.21).", RP, "Executado"),
            ("200-3", "Verificar histórico: PwC de 09/05/2019 a 03/05/2024 e Baker Tilly 4Partners desde 06/05/2024 (FCA p.4) — rodízio compatível "
                      "com período de cinco anos (conferir Res. CVM 23/2021).", RP, "Executado (rodízio: conferência normativa pendente)"),
            ("200-4", "Aplicar o modelo de risco: RDR = RA ÷ (RI × RC). Com RA-alvo de 5% e RI = 1,0 (conservador) e RC = 0,8 (controles não testados), RDR ≈ 6,3% → "
                      "procedimentos substantivos extensos.", SIM, "Executado (parâmetros didáticos)"),
            ("200-5", "Documentar situações de ceticismo (ver quadro abaixo).", RP, "Executado"),
            ("200-6", "Declaração de independência do preparador (aluno) — sem vínculos com Bradespar, Bradesco, Vale ou Baker Tilly.", SIM, "Executado (didático)"),
            ("200-7", "Obter confirmação formal de independência da equipe/rede e lista de relacionamentos.", PLN, "Planejado — sem acesso ao auditor"),
        ],
        "- 200-1/200-2: DF p.42 e p.45; DFP p.21 (Relatório da Administração). 200-3: FCA p.4. Referências cruzadas: PT-220, PT-260 (comunicação sobre independência), PT-315 (riscos).\n"
        "- Cálculo 200-4 reproduzível: `RDR = 0,05/(1,0×0,8) = 0,0625`; ver planilha `Parametros_MUS` (confiança 95%).",
        "**Quadro de ceticismo e julgamento**\n\n" + tab(
            ["Situação", "Postura cética adotada", "Julgamento"],
            [["Relatório sem ressalvas e PAAs conhecidos", "Não tratar como evidência de ausência de erro; reavaliar cada PAA com dados próprios (PT-315, PT-540).", "Risco significativo mantido"],
             ["Expectativa de equivalência diverge do registrado em 12,9% (3,60%) e 7,4% (3,83%)", "Não aceitar explicação genérica; exigir recálculo com participação média ponderada (PT-520).", "Investigação planejada"],
             ["Passivo com acionistas R$ 316.563 mil × R$ 298.450 mil esperados pela Nota 10c", "Tratar diferença de R$ 18.113 mil como indício a investigar, não como erro confirmado.", "Hipótese"],
             ["Reconciliação 'perfeita' da base sintética", "Reconhecer que é propriedade do desenho sintético, não evidência de controle efetivo (PT-500).", "Limitação explícita"]]),
        "Não há, nas fontes públicas, indício de ameaça à independência: nenhum serviço adicional contratado em 2025 e rodízio ocorrido em 2024. O ceticismo é "
        "documentado nos itens acima. O modelo de risco indica RDR baixo e extensão substantiva alta, coerente com a concentração de 91,8% do ativo em uma única "
        "participação avaliada por estimativas da investida.",
        "A independência real só pode ser avaliada com acesso ao auditor; a declaração do aluno é didática. Não foi possível ler a Res. CVM 23/2021 nesta sessão."))

    # ------------------------------------------------------------------ PT-210
    P.append(pt(
        "PT-210", "Termos do trabalho — pré-condições e carta de contratação didática",
        "NBC TA 210 (R1)", "pré-condições da auditoria; concordância com os termos; conteúdo da carta de contratação",
        "Verificar as pré-condições (estrutura de relatório aceitável; responsabilidades da administração) e documentar a carta de contratação **didática** que "
        "formalizaria o trabalho hipotético do preparador.",
        "Risco de aceitar trabalho sem pré-condições: estrutura de relatório inadequada, limitação de escopo ou administração sem reconhecer responsabilidades. "
        "Afeta o nível das DFs.",
        "Fontes: Nota 2 — critérios (DF p.20); relatório do auditor — responsabilidades da administração (DF p.44); declarações dos diretores (DFP p.49–50).",
        [
            ("210-1", "Pré-condição 1 — estrutura de relatório aceitável: CPC/IFRS (Nota 2) e requisitos da Lei 6.404/76 e CVM.", RP, "Executado"),
            ("210-2", "Pré-condição 2 — administração reconhece responsabilidade por elaborar as DFs, controles internos e acesso a informações (texto do relatório, DF p.44–45).", RP, "Executado (indireto)"),
            ("210-3", "Obter reconhecimento formal da administração sobre os termos (assinatura da carta).", PLN, "Planejado — não houve contato com a companhia"),
            ("210-4", "Minuta da carta de contratação didática (abaixo).", SIM, "Executado"),
        ],
        "- 210-1: DF p.20. 210-2: DF p.44. Referências cruzadas: PT-EC, PT-300, PT-580.",
        "**Minuta da carta de contratação (DIDÁTICA — não enviada, não assinada)**\n\n"
        "> À Administração da Bradespar S.A. — Objeto: auditoria das demonstrações financeiras do exercício findo em 31/12/2025, conforme as normas brasileiras e "
        "internacionais de auditoria. Responsabilidades da administração: elaborar e apresentar adequadamente as DFs, manter controles internos necessários, fornecer "
        "acesso a todas as informações, registros e pessoas, e prestar representações formais. Responsabilidades do auditor: obter segurança razoável e emitir relatório. "
        "Limitações inerentes: auditoria não garante a detecção de todas as distorções. Estrutura de relatório: CPC/IFRS. Forma do relatório: relatório do auditor independente. "
        "Honorários e prazo: a definir. **Assinaturas: [reservadas — não simuladas].**",
        "As pré-condições são **atendidas na forma** pelos documentos públicos; o reconhecimento direto pela administração permanece **planejado**. A carta é didática.",
        "Não há contrato real acessível; a minuta não foi enviada nem discutida com ninguém."))

    # ------------------------------------------------------------------ PT-220
    P.append(pt(
        "PT-220", "Gestão da qualidade da auditoria", "NBC TA 220 (R3)",
        "responsabilidades do sócio; requisitos éticos; aceitação/continuidade; recursos; revisão de qualidade do trabalho; consulta",
        "Documentar, em nível de trabalho, como se esperaria gerir a qualidade: liderança do sócio, alocação de equipe, consulta, revisão e (para entidade listada) "
        "revisão de qualidade do trabalho por revisor independente.",
        "Risco de **qualidade insuficiente** em entidade de interesse público: equipe sem competência em investimentos/mineração; ausência de revisão independente; "
        "documentação tardia. Afeta todas as asserções do investimento na Vale.",
        "Fontes: FCA p.4 (auditor e responsável técnico); relatório (DFP p.47: duas assinaturas de contadores e CRC da firma 2SP-031.269/O-1); DFP p.21.",
        [
            ("220-1", "Identificar o responsável técnico e a firma (FCA p.4; DFP p.47).", RP, "Executado"),
            ("220-2", "Verificar sinais públicos de revisão de qualidade: relatório assinado por dois contadores; **não** há informação pública sobre revisor independente.", RP, "Executado (limitado)"),
            ("220-3", "Montar equipe hipotética: sócio, gerente, sênior, assistente e especialista em avaliação/tributos; alocação de horas por PT.", SIM, "Executado (didático)"),
            ("220-4", "Registrar consultas necessárias: (a) CPC 18 — influência significativa após fim do acordo de acionistas da Vale (Nota 8(2)); (b) passivos contingentes.", SIM, "Executado (didático)"),
            ("220-5", "Obter evidência real de políticas da firma (ISQM/NBC PA 01), horas e revisão independente.", PLN, "Planejado — sem acesso"),
        ],
        "- 220-1: FCA p.4; DFP p.47. 220-4: Nota 8(2) (DF p.27). Referências cruzadas: PT-200, PT-230, PT-300.",
        "**Alocação didática de horas (total 260 h)** — Planejamento/PT-3xx: 40 h; Investimento e equivalência (PT-315/330/540/600): 80 h; Base sintética (PT-500/520/530/450): 60 h; "
        "Passivos, caixa e demais: 30 h; Conclusão, comunicações e documentação: 30 h; Revisão de qualidade (hipotética): 20 h.",
        "Nenhum fato público contradiz um ambiente de qualidade adequado; porém sem evidência direta. Conclusão: **qualidade não avaliável com evidência pública**; "
        "os controles de qualidade ficam planejados.",
        "Alocação de horas e equipe são hipóteses; não existe dado público sobre horas ou revisão independente."))

    # ------------------------------------------------------------------ PT-240
    t7a, t7b, t7c, t7d = (int(t(V, x)) for x in ("T7a_manual_fim_semana", "T7b_manual_madrugada", "T7c_usuario_nao_autorizado", "T7d_valor_redondo"))
    P.append(pt(
        "PT-240", "Fraude — fatores de risco, receita, desconsideração de controles pela administração e testes de lançamentos",
        "NBC TA 240 (R2 — publicada em 25/09/2026 segundo a página do CFC; vigência a confirmar)",
        "discussão da equipe; indagações; fatores de risco; presunção de risco na receita; desconsideração de controles; testes de lançamentos manuais; imprevisibilidade",
        "Identificar e avaliar riscos de distorção por fraude, tratar a presunção de risco na **receita** (equivalência e receitas financeiras), o risco de **desconsideração "
        "de controles pela administração** e executar testes de lançamentos manuais sobre a base sintética.",
        "Triângulo da fraude: **pressão** (política de distribuição alta — dividendos e JCP de R$ 1.247.000 mil em 2025 = 228% do lucro de R$ 546.993 mil), **oportunidade** "
        "(entidade com poucos empregados, um único investimento, lançamentos manuais de fechamento) e **racionalização** (não evidenciada). Asserções: ocorrência, "
        "exatidão e corte da equivalência; integridade das distribuições.",
        f"População: {n0(V['n_reg'])} registros sintéticos de lotes (PT-500). Critérios dos testes de lançamento: manuais em fim de semana (T7a), em madrugada 22h–06h (T7b), "
        "por usuário fora da lista autorizada (T7c) e com valores redondos (múltiplos exatos de R$ 5.000,00 — T7d). Fonte pública: DF p.14–19, Nota 10 (p.29–31).",
        [
            ("240-1", "Discussão da equipe sobre suscetibilidade a fraude (agenda didática: pressão de distribuição, lançamentos manuais de fechamento, concentração).", SIM, "Executado (didático)"),
            ("240-2", "Indagações à administração, governança e auditoria interna sobre fraude conhecida ou suspeita.", PLN, "Planejado — sem contato"),
            ("240-3", "Risco de receita: tratar equivalência patrimonial (R$ 571.264 mil) como risco significativo; receitas financeiras (R$ 75.615 mil) — presunção "
                      "**refutável** por fluxo simples (fundo + juros sobre tributos), mas mantida cautela por Outras receitas financeiras de R$ 11.386 mil (Nota 11).", RP, "Executado"),
            ("240-4", "Testes de lançamentos (T7a–T7d) em 100% dos lançamentos da base sintética.", SIM, "Executado (script 02)"),
            ("240-5", "Testes equivalentes no razão geral real (lançamentos manuais, ajustes de fechamento) — exige arquivo do razão.", PLN, "Planejado — sem acesso"),
            ("240-6", "Elemento de imprevisibilidade: incluir testes em datas atípicas e conferência do usuário 'U98/U99' não cadastrado.", SIM, "Executado"),
            ("240-7", "Avaliação de estimativas por viés (equivalência e contingências): comparar premissas ano a ano.", RP, "Executado (PT-540)"),
        ],
        "- 240-3: DF p.15 e p.31 (Nota 11). 240-4: `codigo/02_testes_populacao.py`, `saidas/excecoes_populacao.csv`, planilha `Testes_Populacao`. Cruzamentos: PT-315, PT-330, PT-450, PT-500, PT-530.",
        "**Testes de lançamentos manuais (base sintética):**\n\n" + tab(
            ["Teste", "Registros alertados", "Observação"],
            [["T7a — manual em fim de semana", n0(t7a), "Todos em sábados/domingos de janeiro/2026"],
             ["T7b — manual em madrugada (22h–06h)", n0(t7b), "Horários 23h–03h"],
             ["T7c — usuário fora da lista autorizada", n0(t7c), "U98/U99 não constam da lista U01–U08/SISTEMA; os demais lançamentos suspeitos usam usuários autorizados (U03/U05), por isso T7c alerta só parte"],
             ["T7d — valor redondo", n0(t7d), "Múltiplos exatos de R$ 5.000,00 — improvável como cálculo pro rata"]]) +
        f"\n\nPraticamente o mesmo conjunto de ~200 lançamentos dispara T7a, T7b e T7d (diferença de 1 registro por coincidência de data), o que sugere um **padrão de desconsideração de controles** (valor redondo + fora do horário). "
        f"Efeito monetário estimado desses lançamentos sobre o saldo: {brl(float(t(V, 'T7a_manual_fim_semana', 'efeito_estimado_brl')))}. "
        "Resultado sintético, **não** é constatação sobre a Bradespar real.",
        "Fraude em **receita** tratada como risco significativo para a equivalência (convergente com o PAA do auditor, DF p.43). Na base sintética, os testes de lançamento "
        "identificaram 200 lançamentos manuais suspeitos que devem ser investigados antes de qualquer conclusão (PT-450, PT-265). Para a Bradespar real, a conclusão é "
        "**inconclusiva**: não há acesso ao razão.",
        "Testes de lançamentos reais impossíveis sem o razão; a base sintética mostra a mecânica dos testes, não o risco efetivo. Critérios de horário e fim de semana são premissas do preparador."))

    # ------------------------------------------------------------------ PT-250
    P.append(pt(
        "PT-250", "Leis e regulamentos", "NBC TA 250", "leis e regulamentos com efeito direto/indireto; indagações; leitura de atas; comunicação",
        "Identificar leis e regulamentos com efeito direto nas DFs (societário, tributário, CVM) e realizar **recálculos com evidência pública** das destinações do lucro, "
        "reserva legal, IRRF sobre JCP e limites estatutários.",
        "Risco de **descumprimento** com efeito direto (dividendo mínimo, reserva legal, limites de reserva, tributos) e indireto (litígios fiscais — Notas 9 b-II). Asserções: "
        "apresentação e divulgação; ocorrência; integridade de passivos.",
        "Fontes: Notas 3(g)(h)(i), 9, 10 (DF p.21–23, 27–31); Lei nº 6.404/76 arts. 192 e 199 (citados na Nota 10b); Lei nº 9.249/95 art. 10; Lei nº 15.270/2025; Res. CVM nº 72/22 e 162/22.",
        [
            ("250-1", "Reserva legal: 5% × lucro R$ 546.993 mil = R$ 27.350 mil — confere com DMPL (27.350).", RP, "Executado (recálculo)"),
            ("250-2", "Limite da reserva legal: 20% × capital R$ 5.600.125 mil = R$ 1.120.025 mil ≥ reserva R$ 472.138 mil.", RP, "Executado (recálculo)"),
            ("250-3", "Limite da reserva estatutária: 95% × capital = R$ 5.320.119 mil ≥ saldo R$ 2.535.118 mil.", RP, "Executado (recálculo)"),
            ("250-4", "Dividendo mínimo 30% do lucro ajustado: (JCP líquido 161.197 + dividendos 250.000 + 80.000) = R$ 491.197 mil = 94,5% da base de R$ 519.643 mil (Nota 10c).", RP, "Executado (recálculo)"),
            ("250-5", "IRRF 15% sobre JCP provisionados: 15% × R$ 189.643 mil = R$ 28.446 mil — confere com a Nota 10c.", RP, "Executado (recálculo)"),
            ("250-6", "Contencioso tributário (R$ 979 mi): ler decisão do CARF de 26/11/2025 e avaliar descumprimento potencial (efeito indireto).", RP, "Executado (leitura da nota)"),
            ("250-7", "Indagar a administração/assessores jurídicos sobre descumprimentos conhecidos; ler atas do Conselho e AGO.", PLN, "Planejado — sem acesso"),
            ("250-8", "Impacto da Lei nº 15.270/2025 (tributação de dividendos a partir de 2026) e Reforma Tributária (IBS/CBS) — divulgações na Nota 3(i).", RP, "Executado (leitura)"),
        ],
        "- Recálculos 250-1..250-5: planilha `Concil_Investimento`/`Analiticos` e cálculos neste PT; Notas 10b/10c (DF p.29–31). Referências cruzadas: PT-501 (litígios), PT-550, PT-560.",
        "Todos os recálculos 250-1 a 250-5 **conferem** com as notas e o DMPL. Distribuição total 2025 = R$ 1.247.000 mil (JCP 567.000 + dividendos 680.000), **superior ao lucro** do exercício, "
        "viabilizada pelo uso de reserva estatutária (DMPL, DF p.17) — permitido pelos arts. 192/199 da Lei nº 6.404/76 conforme Nota 10b; atenção ao efeito sobre liquidez (PT-570).",
        "Nenhum descumprimento de lei com efeito direto identificado **com evidência pública**. Efeitos indiretos (autuação IRPJ/CSL de R$ 979 mi; ação Litel R$ 1,4 bi) permanecem como contingências possíveis (PT-501).",
        "Sem acesso a atas, assessores jurídicos ou à administração; interpretação jurídica não foi validada por advogado."))

    # ------------------------------------------------------------------ PT-260
    P.append(pt(
        "PT-260", "Comunicação com os responsáveis pela governança", "NBC TA 260 (R2)",
        "responsáveis pela governança; assuntos a comunicar; independência; forma e época; documentação",
        "Identificar os responsáveis pela governança e planejar a comunicação de escopo, época, constatações significativas e independência, com minuta **didática** de comunicação.",
        "Risco de **comunicação inadequada ou tardia** sobre riscos significativos, distorções não corrigidas e deficiências de controle. Afeta a evidência de supervisão.",
        "Fontes: Órgãos da administração (DF p.41): Conselho de Administração (Presidente, Vice, 5 membros), Conselho Fiscal (5 efetivos/5 suplentes), Diretoria; Parecer do Conselho Fiscal (DFP p.48); "
        "Declarações dos diretores (DFP p.49–50); relatório do auditor (DF p.45–46).",
        [
            ("260-1", "Identificar governança: Conselho de Administração, Conselho Fiscal (parecer de 24/03/2026) — **não** há evidência pública de Comitê de Auditoria.", RP, "Executado"),
            ("260-2", "Verificar sinais de comunicação: diretores declaram concordar com o relatório 'com base no planejamento apresentado pelos auditores e nas discussões subsequentes' (DFP p.49–50).", RP, "Executado"),
            ("260-3", "Verificar que o relatório afirma comunicação de escopo, época, constatações e declaração de independência (DF p.45).", RP, "Executado"),
            ("260-4", "Minuta de comunicação didática (abaixo) com os assuntos do dossiê.", SIM, "Executado"),
            ("260-5", "Obter atas/registros reais da comunicação (data, participantes, assuntos).", PLN, "Planejado — sem acesso"),
        ],
        "- 260-1: DF p.41. 260-2: DFP p.49–50. 260-3: DF p.45. Referências cruzadas: PT-200 (independência), PT-265, PT-450, PT-570.",
        "**Minuta de comunicação (DIDÁTICA — não enviada)**\n\n"
        "1. Escopo e época: auditoria das DFs 2025; PAAs: investimento na Vale e contingências fiscais/cíveis.\n"
        "2. Constatações significativas do dossiê: (i) diferença de R$ " + n0(V['dif_total']) + " entre razão auxiliar **sintético** e saldo do Balanço (PT-500); (ii) 200 lançamentos manuais suspeitos "
        "(PT-240); (iii) indícios analíticos a investigar (PT-520).\n"
        "3. Distorções não corrigidas: ver PT-450. 4. Deficiências de controle: ver PT-265. 5. Independência: declaração didática (PT-200).\n"
        "*(Itens (i)–(iii) referem-se à base sintética/ao exercício didático, não à companhia real.)*",
        "A governança é identificável e há indícios públicos de interação com o auditor; **conteúdo e datas** das comunicações não são públicos. Comunicação didática elaborada.",
        "Sem acesso a atas; a minuta é uma ilustração e não tem destinatário real."))

    # ------------------------------------------------------------------ PT-265
    cmp_tab = V["cmp_tab"]
    P.append(pt(
        "PT-265", "Deficiências de controle interno — matriz de condição, critério, causa, efeito e recomendação",
        "NBC TA 265", "identificação de deficiências; deficiência significativa; comunicação por escrito; recomendações",
        "Consolidar as deficiências **potenciais** e as **constatações apoiadas** em evidência, separando hipóteses (sem evidência) de constatações (sobre a base sintética), e preparar recomendações.",
        "Controles-chave: conciliação razão auxiliar × razão geral; autorização de lançamentos manuais; recálculo da equivalência; controle de dividendos a receber/pagar; segregação "
        "de funções. Risco: distorção relevante não prevenida/detectada.",
        "Fontes: resultados dos testes da base sintética (saidas/ ... ), DF p.14–19, notas 8 e 10. Critério: toda deficiência exige condição observável e critério explícito.",
        [
            ("265-1", "Classificar cada achado da base sintética como constatação (apoiada em evidência sintética) e rotular como **simulada**.", SIM, "Executado"),
            ("265-2", "Registrar hipóteses de controle sobre a Bradespar real (sem evidência) e **não** classificar como deficiência.", RP, "Executado"),
            ("265-3", "Avaliar significância: magnitude (R$ " + n0(V['efeito_liq']) + " líquidos na base), probabilidade e padrão de override.", SIM, "Executado"),
            ("265-4", "Comunicar por escrito deficiências significativas à governança (carta de recomendações).", PLN, "Planejado — sem canal"),
        ],
        "- Achados simulados: `saidas/comparacao_inserido_vs_detectado.csv`; PT-240, PT-450, PT-500, PT-530. Hipóteses: PT-315/520.",
        "**A. Constatações sobre a BASE SINTÉTICA (simuladas)**\n\n" + tab(
            ["ID", "Condição", "Critério", "Causa provável", "Efeito", "Recomendação", "Significância"],
            [["D1", f"Razão auxiliar difere do saldo contábil em {brl(V['dif_total'])}", "Razão auxiliar deve reconciliar com o saldo contábil mensalmente", "Ausência de conciliação periódica", "Superavaliação potencial e conclusão errada sobre saldo",
              "Conciliação mensal com revisão e assinatura", "**Significativa** (padrão e override)"],
             ["D2", "300 registros duplicados (lote lançado duas vezes)", "Unicidade de lote", "Falta de chave única", "Superavaliação", "Restringir chave única no sistema", "Moderada"],
             ["D3", "350 quantidades divergentes da custódia", "Quantidade = extrato do custodiante", "Digitação/ausência de conciliação com custodiante", "Valor errado nas parcelas", "Conciliação diária/semanal de quantidades", "Moderada"],
             ["D4", "200 lançamentos manuais fora do padrão (valor redondo, fim de semana, madrugada, usuários U98/U99)", "Lançamentos manuais autorizados e revisados", "Controle de acesso/autorização insuficiente", "Risco de fraude/override", "Segregação, revisão por alçada, logs", "**Significativa**"],
             ["D5", "150 lançamentos de 2025 após 24/03/2026 (autorização das DFs)", "Corte de período", "Fechamento sem trava", "Risco de ajuste pós-emissão", "Trava de período contábil", "Moderada"],
             ["D6", "80 lotes em conta indevida e 60 com quantidade ≤ 0", "Plano de contas/validação de cadastro", "Ausência de validações de entrada", "Classificação/integridade", "Validações automáticas", "Baixa"],
             ["D7", f"{V['n_nao_det']} lotes com alteração consistente no razão e na custódia (E9) — **não localizáveis linha a linha**", "Total de controle de ações", "Falha comum a razão e extrato", "Subavaliação/superavaliação não detectada por linha", "Conciliação do total de ações com fonte independente (B3/escriturador)", "Moderada"]]) +
        "\n\n**B. Hipóteses sobre a Bradespar real (NÃO são deficiências confirmadas)**\n\n" + tab(
            ["ID", "Hipótese", "Base da hipótese", "Como validar (planejado)"],
            [["H1", "Risco de concentração/key person na contabilização da equivalência (um investimento, equipe pequena)", "Estrutura (Nota 1; DVA)", "Walkthrough do fechamento da equivalência"],
             ["H2", "Diferença entre passivo de dividendos/JCP e Nota 10c: R$ 316.563 mil × R$ 298.450 mil = R$ 18.113 mil sem explicação nas notas", "DF p.14 e p.29–31", "Razão auxiliar do passivo; dividendos não reclamados"],
             ["H3", "Falta de divulgação de transações com partes relacionadas do grupo Bradesco (administração de fundo e escrituração)", "Nota 7(1), FCA p.5, Nota 13", "Indagação; contratos/tarifas"],
             ["H4", "Receita de aplicações (R$ 55.506 mil) acima da expectativa por saldos médios (R$ 21.138 mil)", "Nota 11; PT-520 A4", "Saldos diários do fundo"]]),
        "Na base **sintética**, duas deficiências são consideradas **significativas** (D1 e D4); as demais são moderadas/baixas. Para a Bradespar real, **nenhuma deficiência é afirmada**: "
        "apenas hipóteses a validar.",
        "Deficiências simuladas decorrem de erros inseridos de forma deliberada; não revelam a efetividade dos controles reais. As hipóteses H1–H4 não foram confirmadas."))
    return P
