#!/usr/bin/env bash
# Download the Dienst Toeslagen brochures that carry the official amounts for a
# calendar year (Toeslagenkaart, Informatieblad kindgebonden budget, Berekening
# kinderopvangtoeslag). Usage: fetch_bd_brochures.sh <year> [outdir]
#
# The Belastingdienst "Hoeveel ... krijg ik?" pages no longer print the amount
# tables; these PDFs do. Read them with read_file afterwards and check the
# document code in the footer (e.g. TG 710 / 1Z61PL) matches <year>.
set -uo pipefail

YEAR="${1:?usage: fetch_bd_brochures.sh <year> [outdir]}"
OUT="${2:-/tmp/toeslagen_$YEAR}"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36"
mkdir -p "$OUT"

INDEX_PAGES=(
  "https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/themaoverstijgend/brochures_en_publicaties/toeslagenkaart"
  "https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/themaoverstijgend/brochures_en_publicaties/informatieblad-kindgebonden-budget"
  "https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/themaoverstijgend/brochures_en_publicaties/berekening-kinderopvangtoeslag"
)

: > "$OUT/pdf-links.txt"
for page in "${INDEX_PAGES[@]}"; do
  curl -sSL -A "$UA" --max-time 40 "$page" \
    | grep -oE 'https://download\.belastingdienst\.nl/[^"'\'']+\.pdf' >> "$OUT/pdf-links.txt" || true
done
sort -u -o "$OUT/pdf-links.txt" "$OUT/pdf-links.txt"

echo "# candidates (several years are listed side by side — pick $YEAR):"
cat "$OUT/pdf-links.txt"

while read -r url; do
  [ -n "$url" ] || continue
  curl -sSL -A "$UA" --max-time 60 -o "$OUT/$(basename "$url")" "$url" || true
done < "$OUT/pdf-links.txt"

ls -l "$OUT"
echo
echo "Check each PDF footer code (TG 710 / 1Z6xPL) for $YEAR before quoting amounts."
