# Função para verificar se a string é um palíndromo
def eh_palindromo(s):
    s = s.lower().replace(" ", "")  # Ignora espaços e diferenciação entre maiúsculas e minúsculas
    return s == s[::-1]

# Solicita uma string do usuário
print("Vamos descobrir se a sua string é um palíndromo!")
string_usuario = input("Digite uma string: ")

# Verifica se a string é um palíndromo
if eh_palindromo(string_usuario):
    print(f"\n🎉 Uau! '{string_usuario}' é um palíndromo! 🎉")
else:
    print(f"\n😢 Oh não! '{string_usuario}' não é um palíndromo. 😢")
