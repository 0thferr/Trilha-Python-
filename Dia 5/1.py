# Solicita um número do usuário
numero = float(input("Digite um número: "))

# Verifica se o número é positivo, negativo ou zero
if numero > 0:
    print(f"O número {numero} é positivo! 🌟")
elif numero < 0:
    print(f"O número {numero} é negativo! 🌧️")
else:
    print("Você digitou zero, que é neutro! ⚖️")
