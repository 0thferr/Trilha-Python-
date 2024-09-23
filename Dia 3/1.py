def boas_vindas(nome, idade):
  mensagem = f"""
  ***********************************
  *                                 *
  *   Bem-vindo(a), {nome}!          *
  *   É ótimo saber que você        *
  *   tem {idade} anos.                  *
  *                                 *
  ***********************************
  """
  return mensagem

# Solicita o nome do usuário
nome = input("Por favor, digite seu nome: ")

# Solicita a idade do usuário
idade = input("Por favor, digite sua idade: ")

# Chama a função e imprime a plaquinha de boas-vindas
print(boas_vindas(nome, idade))

