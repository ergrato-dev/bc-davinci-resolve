#!/usr/bin/env bash
# Sella y verifica la integridad del pack de medios del bootcamp.
#
#   ./scripts/preparar-medios.sh --sellar    genera MANIFIESTO.sha256 con la huella
#                                            de cada archivo del pack
#   ./scripts/preparar-medios.sh             comprueba el pack contra el manifiesto
#
# La carpeta del pack se toma de la variable BC_MEDIOS, o del primer argumento.
# Ver docs/pack-de-medios.md.

set -u

SUBCARPETAS=(01-basicos 02-entrevista 03-multicamara 04-log-y-raw 05-croma
             06-audio/musica 06-audio/efectos 06-audio/ambientes 07-graficos)
MANIFIESTO="MANIFIESTO.sha256"

sellar=0
raiz="${BC_MEDIOS:-}"
for arg in "$@"; do
  case "$arg" in
    --sellar) sellar=1 ;;
    -h|--help) sed -n '2,12p' "$0"; exit 0 ;;
    *) raiz="$arg" ;;
  esac
done

if [ -z "$raiz" ]; then
  echo "No sé dónde está tu pack de medios."
  echo "Define BC_MEDIOS o pasa la ruta como argumento:"
  echo "  ./scripts/preparar-medios.sh --sellar <ruta-a-medios>/00-medios-bootcamp"
  exit 2
fi

if [ ! -d "$raiz" ]; then
  echo "La carpeta no existe: $raiz"
  echo "Créala siguiendo docs/pack-de-medios.md."
  exit 2
fi

cd "$raiz" || exit 2

echo "== Estructura =="
faltan=0
for sub in "${SUBCARPETAS[@]}"; do
  if [ -d "$sub" ]; then
    n=$(find "$sub" -type f ! -name ".*" | wc -l)
    printf '  OK  %-22s %s archivo(s)\n' "$sub" "$n"
  else
    printf '  KO  %-22s no existe\n' "$sub"
    faltan=1
  fi
done
[ "$faltan" -eq 1 ] && echo "  Crea las carpetas que faltan antes de sellar."

if [ "$sellar" -eq 1 ]; then
  echo
  echo "== Sellando =="
  find . -type f ! -name "$MANIFIESTO" ! -name ".*" -print0 \
    | sort -z \
    | xargs -0 sha256sum > "$MANIFIESTO"
  echo "  $(wc -l < "$MANIFIESTO") archivo(s) sellados en $raiz/$MANIFIESTO"
  echo "  A partir de ahora, ./scripts/preparar-medios.sh comprueba que siguen intactos."
  exit 0
fi

echo
echo "== Integridad =="
if [ ! -f "$MANIFIESTO" ]; then
  echo "  No hay manifiesto todavía. Cuando termines de descargar, sella el pack:"
  echo "    ./scripts/preparar-medios.sh --sellar"
  exit 0
fi

if sha256sum --quiet -c "$MANIFIESTO"; then
  echo "  OK  los $(wc -l < "$MANIFIESTO") archivos del manifiesto siguen intactos."
  nuevos=$(find . -type f ! -name "$MANIFIESTO" ! -name ".*" | wc -l)
  sellados=$(wc -l < "$MANIFIESTO")
  if [ "$nuevos" -gt "$sellados" ]; then
    echo "  !   hay $((nuevos - sellados)) archivo(s) nuevos sin sellar. Vuelve a sellar cuando termines de añadir material."
  fi
  exit 0
fi

echo
echo "  Los archivos de arriba han cambiado o se han corrompido."
echo "  Si los cambiaste a propósito, vuelve a sellar. Si no, descárgalos otra vez."
exit 1
