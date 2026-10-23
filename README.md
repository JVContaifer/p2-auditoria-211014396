# Dossiê de auditoria — Bradespar S.A. (exercício 2025)

**Matrícula: 211014396** · Trabalho individual (P2) · Entrega: 25/10/2026

> **Aviso importante.** Trabalho acadêmico. **Não é auditoria real nem opinião sobre as demonstrações financeiras.** Não houve contato com a companhia, o auditor, clientes ou fornecedores. A base de 520.000 registros é **SINTÉTICA (fictícia)**: os totais vêm das DFs públicas, mas a divisão em registros e todos os erros são inventados. Nenhuma exceção da base é constatação sobre a Bradespar real.

## O que há aqui
| Pasta/arquivo | Conteúdo |
|---|---|
| `dossie/dossie_auditoria_bradespar_211014396.pdf` | **Dossiê completo** (27 papéis de trabalho com referências cruzadas, programas, matriz de cobertura, fontes, normas, conclusão integrada) |
| `papeis_trabalho/PT-*.md` | Os 27 papéis (EC, 200, 210, 220, 230, 240, 250, 260, 265, 300, 315, 320, 330, 402, 450, 500, 501, 505, 510, 520, 530, 540, 550, 560, 570, 580, 600) |
| `base_simulada/` | Base sintética `.csv.gz` (520.000 linhas), dicionário, gabarito de erros inseridos, hashes, amostra de 1.000 linhas |
| `codigo/` | Gerador da base e scripts de teste, amostragem, comparação, planilhas e dossiê |
| `planilhas/` | `calculos_papeis_de_trabalho.xlsx` (materialidade, conciliações, analíticos, continuidade, MUS, distorções — com fórmulas) e `amostra_MUS.csv` |
| `saidas/` | Resultados dos testes (CSV) e figura |
| `docs/` | Matriz de cobertura NBC TA, fontes (URL/data/página/exercício), versões das normas, programas por ciclo, conclusão integrada, método e hipóteses da base |
| `fontes/` | Cópias dos PDFs públicos usados (DF, DFP, FCA) e `fontes.csv` |

## Empresa
Bradespar S.A. (CNPJ 03.847.461/0001-92; BRAP3/BRAP4). O FCA não informa nome anterior e não foi identificada mudança de ticker. Auditor: Baker Tilly 4Partners (desde 06/05/2024; antes PwC).

## Conta escolhida para a base sintética
**Investimentos (Vale)** — R$ 7.344.756 mil, 91,8% do ativo; é também o principal assunto de auditoria do relatório. Detalhes em `docs/base_sintetica_metodo_e_hipoteses.md`.

## Classificação dos procedimentos
Cada procedimento é *Realizado com evidência pública*, *Planejado por falta de acesso* ou *Simulado para fins didáticos*. Confirmações, entrevistas, inspeções e acesso a sistemas **não** foram realizados.

## Reprodução
```bash
pip install numpy pandas scipy openpyxl matplotlib
bash codigo/00_executar_tudo.sh      # gera base, testes, MUS, planilhas, papéis e PDF (precisa pandoc + xelatex; LibreOffice opcional)
```
Semente 211014396. A base completa em `.csv` (79 MB) não é versionada: use o `.csv.gz` ou rode `codigo/01_gerar_base.py`. Hashes em `base_simulada/hashes.txt`.

## Limitações principais
Dados públicos em cópia PDF; normas não lidas integralmente (ver `docs/NORMAS_VERSOES.md`; NBC TA 240 e 570 com publicação indicada em 25/09/2026, vigência a confirmar); revisão dos papéis deixada em branco (sem assinatura simulada).
