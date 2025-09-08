#!/usr/bin/env bash
set -euo pipefail
trap 'echo "[ERROR] Falló en línea $LINENO" >&2' ERR

mkdir -p reports

# TODO: HTTP — guarda headers y explica código en 2–3 líneas al final del archivo
{
  echo "== curl -I example.com =="
  curl -Is https://example.com | sed '/^\r$/d'
  echo
  echo "Explicación (editar): Código HTTP X significa ..."
} > reports/http.txt

# TODO: DNS — muestra A/AAAA/MX y comenta TTL
{
  echo "== A ==";    dig A example.com +noall +answer
  echo "== AAAA =="; dig AAAA example.com +noall +answer
  echo "== MX ==";   dig MX example.com +noall +answer
  echo
  echo "Nota (editar): TTL alto vs bajo impacta en ..."
} > reports/dns.txt

# TODO: TLS — registra versión TLS
{
  echo "== TLS via curl -Iv =="
  curl -Iv https://example.com 2>&1 | sed -n '1,20p'
} > reports/tls.txt

# TODO: Puertos locales — lista y comenta riesgos
{
  echo "== ss -tuln =="
  ss -tuln || true
  echo
  echo "Riesgos (editar): Puertos abiertos innecesarios pueden ..."
} > reports/sockets.txt

echo "Reportes generados en ./reports"
