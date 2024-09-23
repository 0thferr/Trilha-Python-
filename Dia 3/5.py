import getpass

def obter_escolha_jogador(jogador):
    escolha = getpass.getpass(f"{jogador}, escolha Pedra, Papel ou Tesoura (a escolha não será exibida): ").lower()
    while escolha not in ["pedra", "papel", "tesoura"]:
        escolha = getpass.getpass(f"Escolha inválida. {jogador}, escolha Pedra, Papel ou Tesoura: ").lower()
    return escolha

def determinar_vencedor(escolha1, escolha2):
    if escolha1 == escolha2:
        return "Empate!"
    elif (escolha1 == "pedra" and escolha2 == "tesoura") or \
         (escolha1 == "tesoura" and escolha2 == "papel") or \
         (escolha1 == "papel" and escolha2 == "pedra"):
        return "Jogador 1 vence!"
    else:
        return "Jogador 2 vence!"

def exibir_resultado(escolha1, escolha2, resultado):
    emojis = {"pedra": "🪨", "papel": "📄", "tesoura": "✂️"}
    return f"Jogador 1: {emojis[escolha1]} vs Jogador 2: {emojis[escolha2]}\nResultado: {resultado}"

# Solicita as escolhas dos jogadores
escolha_jogador1 = obter_escolha_jogador("Jogador 1")
print("Jogador 1 fez sua escolha.")
escolha_jogador2 = obter_escolha_jogador("Jogador 2")
print("Jogador 2 fez sua escolha.")

# Determina o vencedor
resultado = determinar_vencedor(escolha_jogador1, escolha_jogador2)

# Exibe o resultado de forma criativa
print(exibir_resultado(escolha_jogador1, escolha_jogador2, resultado))
