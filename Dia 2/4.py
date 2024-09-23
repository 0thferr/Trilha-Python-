# Solicita uma lista de números ao usuário
numeros = input("Digite uma lista de números separados por espaço: ").split()

# Converte os números para inteiros
numeros = [int(numero) for numero in numeros]

# Remove duplicatas preservando a ordem
numeros_unicos = list(dict.fromkeys(numeros))

# Exibe a lista sem duplicatas
print("Lista sem duplicatas:", numeros_unicos)   