from flask import Flask, jsonify, render_template
import requests
import mysql.connector

app = Flask(__name__)

# Configurações do banco de dados
db_config = {
    'host': '172.31.85.144',
    'user': 'root',
    'password': 'tijolo22',
    'database': 'trilha_python_db'
}

# Conectando ao banco de dados
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Função para criar a tabela (CREATE TABLE)
def create_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INT PRIMARY KEY,
            title VARCHAR(255),
            completed BOOLEAN
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()

# Função para criar um registro (CREATE)
def create_record(todo_id, title, completed):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO todos (id, title, completed) VALUES (%s, %s, %s)", (todo_id, title, completed))
    connection.commit()
    cursor.close()
    connection.close()

# Rota para a URL raiz
@app.route('/')
def home():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    data = response.json()
    return render_template('home.html', data=data)

# Rota para fazer a requisição para a API e salvar os dados no banco de dados
@app.route('/fetch-and-save', methods=['GET'])
def fetch_and_save():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    data = response.json()
    
    create_record(data['id'], data['title'], data['completed'])
    
    return jsonify({'message': 'Dados salvos com sucesso!'})

if __name__ == '__main__':
    create_table()
    app.run(host="0.0.0.0", debug=True)
