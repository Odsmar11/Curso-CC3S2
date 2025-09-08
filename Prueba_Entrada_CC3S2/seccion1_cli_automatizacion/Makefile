SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c

.PHONY: help tools report all
help: ## Mostrar ayuda
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | sed 's/:.*##/: /'

tools: ## Verifica binarios requeridos
	@for b in git bash make python3 pytest curl dig ss jq; do \
	  command -v $$b >/dev/null || { echo "Falta $$b"; exit 1; }; \
	done
	@echo "OK herramientas"

report: ## Genera reportes HTTP/DNS/TLS/puertos
	@bash scripts/syscheck.sh

all: tools report ## Ejecuta todo
