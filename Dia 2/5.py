def soma(x, y):
  return x + y

def subtracao(x, y):
  return x - y

def multiplicacao(x, y):
  return x * y

def divisao(x, y):
  if y != 0:
      return x / y
  else:
      return "Erro! Divisão por zero."

while True:
  print("\nSelecione a operação:")
  print("1. Soma")
  print("2. Subtração")
  print("3. Multiplicação")
  print("4. Divisão")
  print("0. Sair")

  escolha = input("Digite a opção (1/2/3/4/0): ")

  if escolha == '0':
      print("Saindo...")
      break

  if escolha in ['1', '2', '3', '4']:
      num1 = float(input("Digite o primeiro número: "))
      num2 = float(input("Digite o segundo número: "))

      if escolha == '1':
          print(f"Resultado: {num1} + {num2} = {soma(num1, num2)}")
      elif escolha == '2':
          print(f"Resultado: {num1} - {num2} = {subtracao(num1, num2)}")
      elif escolha == '3':
          print(f"Resultado: {num1} * {num2} = {multiplicacao(num1, num2)}")
      elif escolha == '4':
          print(f"Resultado: {num1} / {num2} = {divisao(num1, num2)}")
  else:
      print("Opção inválida. Tente novamente.")
