# Função para encontrar o maior número
def encontrar_maior(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Solicita três números do usuário
print("Vamos descobrir qual é o maior número!")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Encontra o maior número
maior_numero = encontrar_maior(numero1, numero2, numero3)

# Imprime o resultado de forma criativa
print(f"\n🎉 O maior número entre {numero1}, {numero2} e {numero3} é {maior_numero}! 🎉")
