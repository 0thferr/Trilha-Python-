# Solicita uma string do usuário
frase = input("Digite uma frase: ")

# Conta o número de palavras na string
numero_palavras = len(frase.split())

# Exibe o número de palavras com uma mensagem personalizada
print(f"A frase contém {numero_palavras} palavras.")

# Mensagem personalizada baseada no número de palavras
if numero_palavras == 1:
    print("Você digitou uma palavra solitária! 🕵️‍♂️")
elif numero_palavras < 5:
    print("Uma frase curta e doce! 🍬")
elif numero_palavras < 10:
    print("Uma frase de tamanho médio! 📏")
else:
    print("Uau, que frase longa! 📜")
