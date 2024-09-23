import time

print("Números pares entre 1 e 100:")
for numero in range(1, 101):
    if numero % 2 == 0:
        print(f"{numero:3} | {'=' * (numero // 2)}")
        time.sleep(0.1)  # Pausa para criar um efeito de animação
