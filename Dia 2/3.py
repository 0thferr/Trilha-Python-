# Solicita um número ao usuário
numero = int(input("Digite um número para calcular o fatorial: "))

# Inicializa a variável fatorial
fatorial = 1

# Calcula o fatorial usando um loop for
for i in range(1, numero + 1):
    fatorial *= i

# Exibe o resultado
print(f"O fatorial de {numero} é {fatorial}.")