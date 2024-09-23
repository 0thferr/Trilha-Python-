def contar_vogais_consoantes(string):
    vogais = "aeiouAEIOU"
    num_vogais = 0
    num_consoantes = 0

    for char in string:
        if char.isalpha():
            if char in vogais:
                num_vogais += 1
            else:
                num_consoantes += 1

    return num_vogais, num_consoantes

def exibir_resultado(vogais, consoantes):
    grafico_vogais = 'Vogais: ' + '🔵' * vogais
    grafico_consoantes = 'Consoantes: ' + '🔴' * consoantes
    return f"{grafico_vogais}\n{grafico_consoantes}"

# Solicita a string do usuário
string = input("Digite uma string: ")

# Conta o número de vogais e consoantes
num_vogais, num_consoantes = contar_vogais_consoantes(string)

# Exibe o resultado de forma criativa
print(exibir_resultado(num_vogais, num_consoantes))

