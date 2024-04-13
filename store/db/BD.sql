CREATE TABLE usuarios (
    id INT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    permissao VARCHAR(255)
);

-- Criar a tabela de produtos
CREATE TABLE produtos (
    id INT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10, 2) NOT NULL
);

-- Inserir usuário 1
INSERT INTO usuarios (id, nome, senha, permissao) VALUES (1, 'usuario1', 'senha1', 'admin');

-- Inserir usuário 2
INSERT INTO usuarios (id, nome, senha, permissao) VALUES (2, 'usuario2', 'senha2', 'normal');

-- Inserir usuário 3
INSERT INTO usuarios (id, nome, senha, permissao) VALUES (3, 'usuario3', 'senha3', 'normal');
