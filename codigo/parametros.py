"""Parâmetros comuns (valores PÚBLICOS extraídos das demonstrações financeiras da Bradespar S.A. de 31/12/2025).
Fonte: Demonstrações Financeiras Bradespar 2025 (arquivo 'Demonstrações Financeiras'), Notas 8 e 13, e DFP/CVM de 31/12/2025.
Todos os valores monetários em R$ (as DFs são em R$ mil; aqui multiplicados por 1.000).
"""
MATRICULA = "211014396"
SEED = int(MATRICULA)            # semente determinística = matrícula

# --- Balanço e movimentação da conta Investimentos (Nota 8 / DMPL / Nota 13) ---
SALDO_INICIAL = 8_153_681_000     # Investimentos 31/12/2024
EQUIVALENCIA  =   571_264_000     # Resultado de equivalência patrimonial 2025
OCI_REFLEXO   =  -135_589_000     # Reflexos de empresas com influência significativa (DMPL/DRA)
JCP_BRUTO     =  -566_011_000     # JCP recebidos (309.620) + a receber (256.391), brutos de IRRF (Nota 13)
DIVIDENDOS    =  -678_589_000     # Dividendos recebidos (349.881) + a receber (328.708) (Nota 13)
SALDO_FINAL   =  7_344_756_000    # Investimentos 31/12/2025 (Balanço, Nota 8)
QTD_ACOES     =  163_355_000      # Nota 8: 163.355 mil ações ON da Vale (arredondado a milhar; o valor exato não consta das fontes primárias coletadas)

assert SALDO_INICIAL + EQUIVALENCIA + OCI_REFLEXO + JCP_BRUTO + DIVIDENDOS == SALDO_FINAL

# --- Demais valores públicos usados nos papéis de trabalho (R$ mil) ---
DF = dict(
    ativo_total=7_999_560, ativo_circ=565_128, caixa=18_402, div_receber=546_640, desp_antec=44, outros_ac=42,
    ativo_nc=7_434_432, rlp_tributos=84_710, imobilizado=899, intangivel=4_067, investimentos=7_344_756,
    investimentos_2024=8_153_681, ativo_total_2024=8_606_884, caixa_2024=287_950, div_receber_2024=72_276,
    passivo_circ=347_821, passivo_nc=3_968, pl=7_647_771, pl_2024=8_483_367,
    div_jcp_pagar=316_563, outras_obrig=30_034, salarios=471, impostos_recolher=391, arrend_c=362, arrend_nc=3_968,
    capital=5_600_125, reservas=3_007_256, aap=-959_610,
    eq_pat=571_264, eq_pat_2024=1_187_822, dga=-34_541, dga_2024=-26_286, desp_trib=-64_815, desp_trib_2024=-42_823,
    res_fin=75_085, res_fin_2024=57_639, rec_fin=75_615, lucro=546_993, lucro_2024=1_192_208,
    dfc_op=670_015, dfc_op_2024=790_041, dfc_fin=-939_563, dfc_fin_2024=-747_196, dfc_jcp_receb=685_334,
    dfc_jcp_receb_2024=738_081, var_caixa=-269_548,
    vale_pl=188_926_000, vale_lucro_atrib=13_814_281, vale_ativo=476_094_000, vale_receita=213_595_000,
    particip_dir=0.0360, particip_ex_tesouraria=0.0383,
    mercado_vale=11_754_997, mercado_vale_2024=8_910_993,
    jcp_receb=309_620, jcp_receber=256_391, div_receb=349_881, div_receber_vale=328_708,
    irrf_jcp_receber=38_459,
    remuneracao_adm=18_660, remuneracao_adm_2024=15_000,
    cred_trib_nao_ativados=355_800,
)
DATA_EMISSAO_DF = "2026-03-24"     # autorização do Conselho de Administração e relatório do auditor
DATA_BASE = "2025-12-31"
