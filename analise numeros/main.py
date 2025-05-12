import math

def analisar_lista(numeros):
    if not numeros:
        return "a lista está vazia."

    total = len(numeros)
    soma = sum(numeros)
    media = math.floor((soma / total) * 100) / 100
    maior = max(numeros)
    menor = min(numeros)
    pares = [n for n in numeros if n % 2 == 0]

    return {
        "média": media,
        "maior número": maior,
        "menor número": menor,
        "quantidade de números pares": len(pares)
    }

