# Base sintética — escolha da conta, método de geração, hipóteses e reconciliação

> **TODOS OS REGISTROS DA BASE SÃO SINTÉTICOS (FICTÍCIOS).** Os totais vêm das DFs públicas; a divisão em registros individuais é artificial.

## 1. Conta de maior materialidade do ativo
Das contas do ativo em 31/12/2025 (DF p.14), **Investimentos (Nota 8) = R$ 7.344.756 mil = 91,8% do ativo total (R$ 7.999.560 mil)**; a segunda é *Dividendos e JCP a receber* (R$ 546.640 mil; 6,8%). O investimento é também o PAA do auditor (DF p.43) e o risco central (PT-315). Portanto a base sintética representa o **razão auxiliar do investimento na Vale**.

## 2. Unidade (registro individual)
Cada linha é um **sublote de custódia** de ações ordinárias da Vale (VALE3), com quantidade, parcelas do roll-forward 2025 e atributos de lançamento (data, hora, usuário). **Hipótese A1:** a fragmentação é fictícia — a Bradespar contabiliza uma única linha de investimento; a decomposição permite exercitar amostragem e testes de população em 520.000 registros (519.700 lotes únicos + 300 duplicidades inseridas).

## 3. Hipóteses
- **A2** — Quantidade total de 163.355.000 ações (Nota 8 informa 163.355 mil; valor exato não consta das fontes coletadas).
- **A3** — Datas de origem (01/08/2017–31/12/2024) e custodiantes (C01–C06) são fictícios.
- **A4** — Conta contábil 1.2.1.01 é fictícia.
- **A5** — Datas/horas/usuários de lançamento são fictícios (97% automáticos pelo SISTEMA; 3% manuais por U01–U08, dias úteis 08h–18h).
- **A6** — O balanço publicado é tratado como ponto de comparação; diferenças entre o razão auxiliar sintético e o balanço **não** são achados sobre a Bradespar real.
- **A7** — Cada parcela do roll-forward é alocada **pro rata** à quantidade (maior resto, em centavos), de modo que a soma dos registros limpos reproduz exatamente os totais públicos: saldo inicial R$ 8.153.681.000; equivalência R$ 571.264.000; OCI −R$ 135.589.000; JCP −R$ 566.011.000; dividendos −R$ 678.589.000; saldo final R$ 7.344.756.000.

## 4. Erros inseridos (gabarito `registro_erros_inseridos.csv`)
| tipo_erro | natureza | inseridos | efeito_inserido_brl | detectados_populacao |
|---|---|---|---|---|
| E1a | valor | 400 | 120487.18 | 400 |
| E1b | valor | 300 | -9685.25 | 300 |
| E2 | valor | 350 | 13918505.08 | 350 |
| E3 | valor | 300 | 4759984.35 | 300 |
| E4 | corte | 150 | 172027.94 | 150 |
| E5 | valor | 200 | 8365652.19 | 200 |
| E6 | integridade | 60 | 0.0 | 60 |
| E7 | valor | 40 | -345037.87 | 40 |
| E8 | classificacao | 80 | -832874.79 | 80 |
| E9 | valor | 150 | 661749.88 | 0 |
| TOTAL |  | 2030 | 26810808.71 | 1880 |

Descrição: **E1a** equivalência com taxa errada; **E1b** erro de soma; **E2** quantidade diverge da custódia; **E3** duplicidade de lote; **E4** lançamento após 24/03/2026 (corte); **E5** lançamentos manuais suspeitos (valor redondo, fim de semana, madrugada, usuário não autorizado); **E6** quantidade ≤ 0; **E7** baixa indevida (saldo zero); **E8** conta indevida; **E9** alteração consistente em razão e custódia (não localizável por linha).

## 5. Reconciliação com o saldo contábil
| Item | Valor (R$) |
|-----------------------------------------------------------------------|-----------------------------|
| Saldo contábil — Balanço 31/12/2025 (Investimentos) | 7.344.756.000,00 |
| (+) Duplicidades (T3) | 4.759.984,35 |
| (+/−) Quantidade registrada diverge da custódia (T2) | 13.918.504,78 |
| (+/−) Valores sem aderência ao pro rata/soma (T1, T5, T8) | 8.131.091,29 |
| (+) Excesso de ações no total de controle (T0): 14,718 ações × R$ 44.9619 — NÃO localizado por linha | 661.749,68 |
| Total: saldo esperado do razão auxiliar (todas as contas) | 7.372.227.330,10 |
| Soma observada do razão auxiliar (todas as contas) | 7.372.227.655,56 |
| Diferença residual não explicada (arredondamento/precisão) | 325,46 |
| (−) Registros em conta indevida (T9) | -832.874,79 |
| Total: soma do razão auxiliar na conta 1.2.1.01 | 7.371.394.780,77 |
| Diferença total da conta 1.2.1.01 vs. Balanço | 26.638.780,77 |

A diferença bruta entre o razão sintético (R$ 7.372.227.655,56) e o balanço (R$ 7.344.756.000,00) é de **R$ 27.471.655,56** e é explicada pelos erros identificados pelos testes (diferença residual por arredondamento). Em dados reais, essa explicação completa **não** seria esperada.

## 6. Reprodução
`python3 codigo/01_gerar_base.py` (semente 211014396; numpy/pandas) gera os mesmos arquivos; verifique `base_simulada/hashes.txt`. Os hashes dependem de versões compatíveis de numpy/pandas.
