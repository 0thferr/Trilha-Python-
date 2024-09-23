def maior_numero(lista):
  if not lista:
      return None
  maior = lista[0]
  for numero in lista:
      if numero > maior:
          maior = numero
  return maior

# Exemplo de uso
numeros = [10, 20, 30, 40, 50, 60, 80, 90, 100]
print("O maior número entre 10 á 100 é:", maior_numero(numeros))
