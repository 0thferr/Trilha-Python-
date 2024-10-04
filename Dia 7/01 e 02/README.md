# Projeto MySQL

Este projeto contém scripts SQL para criar um banco de dados, uma tabela e inserir dados de usuários.

## Estrutura de Pastas

- **/01**: Contém os scripts SQL.
  - **banco_de_dados.sql**: Script para criar o banco de dados.
  - **tabela.sql**: Script para criar a tabela.
  - **dados.sql**: Script para inserir os dados na tabela.

## Como Usar

1. Execute `banco_de_dados.sql` para criar o banco de dados.
2. Execute `tabela.sql` para criar a tabela.
3. Execute `dados.sql` para inserir os registros de usuários.
4. Execute `mysql -h 172.31.85.144 -u root -p` para conectar-se ao banco de dados
5. Execute `USE trilha_python_db;` para selecionar o banco de dados
6. Execute `SHOW TABLES;` para verificar as tabelas
7. Execute `SELECT * FROM users;` para listar os dados da tabela




