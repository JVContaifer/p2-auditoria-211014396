#!/usr/bin/env bash
# Converte dossie/dossie_completo.md em PDF (pandoc + xelatex). Requer pandoc, xelatex e fontes DejaVu.
set -euo pipefail
export LC_ALL=C.UTF-8 LANG=C.UTF-8
cd "$(dirname "$0")/../dossie"
pandoc dossie_completo.md -o dossie_auditoria_bradespar_211014396.pdf \
  --pdf-engine=xelatex --from markdown-tex_math_dollars+pipe_tables+raw_tex \
  -H cabecalho.tex --toc --toc-depth=1 \
  -V mainfont="DejaVu Serif" -V sansfont="DejaVu Sans" -V monofont="DejaVu Sans Mono" -V fontsize=10pt \
  -V geometry:margin=1.9cm -V geometry:a4paper -V fontfamily=etoolbox -V lang=pt-BR -V colorlinks=true -V linkcolor=blue \
  --metadata-file=meta.yaml 2>&1 | grep -v "^$" | head -20 || true
ls -la dossie_auditoria_bradespar_211014396.pdf
