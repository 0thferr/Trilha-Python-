import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Erro:', response.status_code)
