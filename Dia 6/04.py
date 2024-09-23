import requests

# Lista de URLs
urls = [
    'https://jsonplaceholder.typicode.com/todos/1',
    'https://jsonplaceholder.typicode.com/todos/2',
    'https://jsonplaceholder.typicode.com/todos/3'
]

# Itera sobre a lista de URLs
for url in urls:
    try:
        # Faz a requisição HTTP
        response = requests.get(url)
        # Imprime o status de resposta
        print(f'URL: {url} - Status: {response.status_code}')
    except requests.exceptions.RequestException as e:
        # Captura e imprime qualquer erro que ocorra durante a requisição
        print(f'Erro ao acessar {url}: {e}')
