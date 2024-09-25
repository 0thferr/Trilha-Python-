from flask import Flask, jsonify
from flask_mysqldb import MySQL
import requests

app = Flask(__name__)

# Importando as configurações do MySQL
app.config.from_pyfile('config.py')

mysql = MySQL(app)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <style>
                .caixa {
                    border: 2px solid #4CAF50;
                    padding: 20px;
                    margin: 20px;
                    text-align: center;
                    font-family: Arial, sans-serif;
                    background-color: #f9f9f9;
                    box-shadow: 2px 2px 12px #aaa;
                }
            </style>
        </head>
        <body>
            <div class="caixa">
                <h1>Bem-vindo à aplicação Flask!</h1>
            </div>
        </body>
    </html>
    '''

@app.route('/atualizar_dados')
def atualizar_dados():
    # Fazendo a requisição para a API
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    dados = response.json()

    # Salvando os dados no MySQL
    cur = mysql.connection.cursor()
    for item in dados:
        nome = item['nome']
        valor = item['valor']
        cur.execute("INSERT INTO dados_api (nome, valor) VALUES (%s, %s)", (nome, valor))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Dados atualizados com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)

