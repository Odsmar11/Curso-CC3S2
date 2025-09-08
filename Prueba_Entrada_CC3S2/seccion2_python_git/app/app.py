# Implementa la función summarize y el CLI.
# Requisitos:
# - summarize(nums) -> dict con claves: count, sum, avg
# - Valida que nums sea lista no vacía y elementos numéricos (acepta strings convertibles a float).
# - CLI: python -m app "1,2,3" imprime: sum=6.0 avg=2.0 count=3
def summarize(nums):
    if not isinstance(nums, list):
        raise TypeError("nums debe ser una lista")
    if not nums:
        raise ValueError("nums no puede ser una lista vacía")
    valores = []
    for i, v in enumerate(nums):
        try:
            valores.append(float(v))
        except Exception:
            raise ValueError(f"Elemento en posición {i} no es numérico: {v!r}")
    total = sum(valores)
    count = len(valores)
    avg = total / count
    return {"count": count, "sum": total, "avg": avg}
if __name__ == "__main__":
    import sys
    raw = sys.argv[1] if len(sys.argv) > 1 else ""
    items = [p.strip() for p in raw.split(",") if p.strip()]
    result = summarize(items)
    print(f"sum={result['sum']} avg={result['avg']} count={result['count']}")
