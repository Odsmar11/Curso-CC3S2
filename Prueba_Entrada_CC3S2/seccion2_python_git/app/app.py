# Implementa la función summarize y el CLI.
# Requisitos:
# - summarize(nums) -> dict con claves: count, sum, avg
# - Valida que nums sea lista no vacía y elementos numéricos (acepta strings convertibles a float).
# - CLI: python -m app "1,2,3" imprime: sum=6.0 avg=2.0 count=3

def summarize(nums):  # TODO: tipado opcional
    raise NotImplementedError("Implementa summarize según el enunciado")


if __name__ == "__main__":
    import sys
    raw = sys.argv[1] if len(sys.argv) > 1 else ""
    items = [p.strip() for p in raw.split(",") if p.strip()]
    # TODO: validar items y llamar summarize, luego imprimir el formato solicitado
    print("TODO: implementar CLI (python -m app \"1,2,3\")")
