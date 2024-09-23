def criar_tabuleiro(tamanho):
  return [[' ' for _ in range(tamanho)] for _ in range(tamanho)]

def imprimir_tabuleiro(tabuleiro):
  for linha in tabuleiro:
      print(' '.join(linha))
  print()

def pode_colocar_palavra(tabuleiro, palavra, linha, coluna, direcao):
  if direcao == 'H':
      if coluna + len(palavra) > len(tabuleiro[0]):
          return False
      for i in range(len(palavra)):
          if tabuleiro[linha][coluna + i] not in (' ', palavra[i]):
              return False
  elif direcao == 'V':
      if linha + len(palavra) > len(tabuleiro):
          return False
      for i in range(len(palavra)):
          if tabuleiro[linha + i][coluna] not in (' ', palavra[i]):
              return False
  return True

def colocar_palavra(tabuleiro, palavra, linha, coluna, direcao):
  if direcao == 'H':
      for i in range(len(palavra)):
          tabuleiro[linha][coluna + i] = palavra[i]
  elif direcao == 'V':
      for i in range(len(palavra)):
          tabuleiro[linha + i][coluna] = palavra[i]

def jogo_palavras_cruzadas(palavras):
  tamanho = 15
  tabuleiro = criar_tabuleiro(tamanho)

  for palavra in palavras:
      colocada = False
      for linha in range(tamanho):
          for coluna in range(tamanho):
              if pode_colocar_palavra(tabuleiro, palavra, linha, coluna, 'H'):
                  colocar_palavra(tabuleiro, palavra, linha, coluna, 'H')
                  colocada = True
                  break
              elif pode_colocar_palavra(tabuleiro, palavra, linha, coluna, 'V'):
                  colocar_palavra(tabuleiro, palavra, linha, coluna, 'V')
                  colocada = True
                  break
          if colocada:
              break

  imprimir_tabuleiro(tabuleiro)

# Solicita uma lista de palavras do usuário
palavras = input("Digite uma lista de palavras separadas por espaço: ").split()

# Executa o jogo de palavras cruzadas
jogo_palavras_cruzadas(palavras)
