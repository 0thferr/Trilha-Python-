import requests

# Faz a requisição para a API
response = requests.get('https://jsonplaceholder.typicode.com/users')

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    users = response.json()
    # Itera sobre a lista de usuários e imprime o nome de cada um
    for user in users:
        print(user['name'])
else:
    print('Erro:', response.status_code)
