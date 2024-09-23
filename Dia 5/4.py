# Solicita uma lista de números do usuário
numeros = input("Digite uma lista de números separados por espaço: ").split()

# Converte a lista de strings para uma lista de números
numeros = [float(num) for num in numeros]

# Calcula a soma dos números, excluindo os negativos
soma_positivos = sum(num for num in numeros if num >= 0)

# Exibe a soma com uma mensagem personalizada
print(f"A soma dos números positivos é: {soma_positivos}")

# Mensagem personalizada baseada na soma
if soma_positivos > 0:
    print("Ótimo trabalho! Você tem uma soma positiva! 🎉")
elif soma_positivos == 0:
    print("A soma é zero, parece que todos os números eram negativos ou zero! ⚖️")
else:
    print("Hmm, algo deu errado. A soma não deveria ser negativa! 🤔")
