# Solicita três números do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Calcula a média dos três números
media = (numero1 + numero2 + numero3) / 3

# Exibe a média com uma mensagem personalizada
print(f"A média dos números {numero1}, {numero2} e {numero3} é {media:.2f}.")

# Mensagem personalizada baseada na média
if media > 0:
    print("A média é positiva! 🌞")
elif media < 0:
    print("A média é negativa! 🌧️")
else:
    print("A média é zero, um ponto de equilíbrio! ⚖️")
