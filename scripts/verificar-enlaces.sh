#!/usr/bin/env bash
# Verifica integridad estructural del bootcamp:
#   1. Nombres de carpeta week-NN-slug bien formados (36 semanas, single-track).
#   2. Enlaces relativos en markdown que resuelven a una ruta real.
#   3. Sección "Navegación" en el README de cada semana.
#   4. SVG de 0-assets/ enlazados desde algún .md.
#   5. checks.json válido como JSON.
#
# Uso: scripts/verificar-enlaces.sh
# Salida: lista de problemas encontrados; exit code 1 si hay al menos uno.

set -u
cd "$(dirname "$0")/.." || exit 1

fail=0

echo "== 1. Nombres de carpeta =="
while IFS= read -r d; do
  name=$(basename "$d")
  if ! [[ "$name" =~ ^week-[0-9]{2}-[a-z0-9_]+$ ]]; then
    echo "NOMBRE INVALIDO (week): $d"
    fail=1
  fi
done < <(find bootcamp -mindepth 1 -maxdepth 1 -type d -iname "week-*")

echo "== 2. Enlaces relativos en markdown =="
# ponytail: no parsea markdown de verdad, solo strip de fences ``` y luego
# grep de enlaces "](...)" . Falsos positivos conocidos: URLs con paréntesis
# anidados (ej. wikipedia "(film)"). Si el script reporta algo distinto a
# eso, es un enlace roto real.
while IFS= read -r f; do
  content=$(awk '/^```/{c=!c; next} !c' "$f")
  while IFS= read -r link; do
    [ -z "$link" ] && continue
    clean="${link%%#*}"
    [ -z "$clean" ] && continue
    case "$clean" in http*|\<http*|mailto:*|\#*|/*) continue ;; esac
    dir=$(dirname "$f")
    resolved=$(realpath -m "$dir/$clean")
    if [ ! -e "$resolved" ]; then
      echo "ENLACE ROTO: $f -> $link"
      fail=1
    fi
  done < <(printf '%s\n' "$content" | grep -oE '\]\([^)]+\)' | sed -E 's/^\]\(//;s/\)$//')
# .claude/ y .github/prompts/ contienen plantillas con rutas de ejemplo
# (`[texto](ruta)`, `../0-assets/NN-nombre.svg`) que no resuelven por diseño.
done < <(find . -iname "*.md" -not -path "./.git/*" -not -path "*/node_modules/*" \
           -not -path "./.claude/*" -not -path "./.github/prompts/*")

echo "== 3. Navegación anterior/siguiente en README de cada semana =="
while IFS= read -r rm; do
  if ! grep -q "Navegación" "$rm"; then
    echo "SIN NAVEGACION: $rm"
    fail=1
  fi
done < <(find bootcamp -mindepth 2 -maxdepth 2 -iname "README.md")

echo "== 4. SVG huérfanos en 0-assets/ =="
while IFS= read -r svg; do
  base=$(basename "$svg")
  if ! grep -rqF "$base" --include="*.md" .; then
    echo "SVG HUERFANO (no enlazado desde ningún .md): $svg"
    fail=1
  fi
done < <(find bootcamp assets -iname "*.svg" 2>/dev/null)

echo "== 5. checks.json válido =="
while IFS= read -r cj; do
  if ! jq -e . "$cj" > /dev/null 2>&1; then
    echo "JSON INVALIDO: $cj"
    fail=1
  fi
done < <(find bootcamp -name "checks.json")

if [ "$fail" -eq 0 ]; then
  echo "OK: sin problemas detectados."
fi
exit "$fail"
