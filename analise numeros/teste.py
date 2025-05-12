from main import analisar_lista

numeros = [10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]
resultado = analisar_lista(numeros)

for chave, valor in resultado.items():
    if chave == "média":
        print(f"{chave}: {valor:.2f}")
    else:
        print(f"{chave}: {valor}")