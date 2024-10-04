-- Usar o banco de dados
USE banco_de_dados;

-- Criar a tabela usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    uid INT PRIMARY KEY,
    gid INT,
    grupos VARCHAR(255)
);
