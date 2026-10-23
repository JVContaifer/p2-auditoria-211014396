#!/usr/bin/env bash
# Reproduz TODO o pipeline (base sintética -> testes -> amostra -> comparação -> planilhas -> papéis de trabalho -> dossiê PDF)
# Requisitos: python3 (numpy, pandas, scipy, openpyxl, matplotlib), pdflatex, LibreOffice (opcional, para recalcular fórmulas da planilha)
set -euo pipefail
cd "$(dirname "$0")/.."
python3 codigo/01_gerar_base.py
python3 codigo/02_testes_populacao.py
python3 codigo/03_amostragem_mus.py
python3 codigo/04_comparacao.py
python3 codigo/05_planilhas.py
# recalcula as fórmulas (valores em cache) se o LibreOffice existir
if command -v soffice >/dev/null 2>&1; then
  rm -rf /tmp/recalc_xlsx && soffice --headless --convert-to xlsx:"Calc MS Excel 2007 XML" --outdir /tmp/recalc_xlsx planilhas/calculos_papeis_de_trabalho.xlsx >/dev/null 2>&1 \
   && cp /tmp/recalc_xlsx/calculos_papeis_de_trabalho.xlsx planilhas/calculos_papeis_de_trabalho.xlsx
fi
python3 codigo/08_figuras.py
python3 codigo/06_gerar_papeis.py
bash codigo/07_montar_dossie.sh
