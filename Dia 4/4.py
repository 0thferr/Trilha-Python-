import time

# Função para calcular a sequência de Fibonacci
def fibonacci_ate(n):
    sequencia = [0, 1]
    while sequencia[-1] + sequencia[-2] <= n:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

# Solicita um número do usuário
print("Vamos calcular a sequência de Fibonacci!")
numero = int(input("Digite um número: "))

# Calcula a sequência de Fibonacci
sequencia_fibonacci = fibonacci_ate(numero)

# Imprime a sequência de forma criativa
print("\nCalculando a sequência de Fibonacci...\n")
for num in sequencia_fibonacci:
    print(f"{num} ", end="", flush=True)
    time.sleep(0.5)  # Pausa para criar um efeito de animação

print("\n\nSequência de Fibonacci completa! 🎉")
