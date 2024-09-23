def calcular_media(numeros):
  return sum(numeros) / len(numeros)

def exibir_grafico(media):
  barras = int(media) * '|'
  return f"Média: {media:.2f}\n{barras}"

# Solicita a lista de números do usuário
numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [float(num) for num in numeros]

# Calcula a média
media = calcular_media(numeros)

# Exibe a média de forma criativa
print(exibir_grafico(media))
