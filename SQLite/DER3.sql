BEGIN TRANSACTION;

DROP TABLE IF EXISTS Marcas;
DROP TABLE IF EXISTS Modelos;
DROP TABLE IF EXISTS Carros;
DROP TABLE IF EXISTS Vendedores;
DROP TABLE IF EXISTS Pedidos;
DROP TABLE IF EXISTS Itens_pedidos;
DROP TABLE IF EXISTS Clientes;
DROP TABLE IF EXISTS Cidades;
DROP TABLE IF EXISTS UF;


CREATE TABLE Marcas(
    MarcasID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Sitio TEXT NOT NULL
);

CREATE TABLE Modelos(
    ModelosID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL
);

CREATE TABLE Carros(
    CarrosID INTEGER PRIMARY KEY AUTOINCREMENT,
    Ano INTEGER,
    Versao INTEGER,
    Cor TEXT NOT NULL,
    MarcasID INTEGER
);

CREATE TABLE Vendedores(
    VendedorID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Data_nascimento DATE,
    Endereco INTEGER,
    Fone TEXT NOT NULL
);

CREATE TABLE Pedidos(
    PedidosID INTEGER PRIMARY KEY AUTOINCREMENT,
    Numero_pedido INTEGER,
    Data_pedido date,
    VendedorID INTEGER,
    ClienteID INTEGER,
    Valor_unitario REAL,
    Valor_total REAL
);

CREATE TABLE Itens_pedidos(
    Numero_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
    Sequencia TEXT NOT NULL,
    Quantidade INTEGER,
    Produto INTEGER,
    Valor_unitario REAL,
    Valor_total REAL
);

CREATE TABLE Clientes(
    ClienteID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Data_nasciemtno  date,
    Endereco INTEGER,
    Fone TEXT NOT NULL
);

CREATE TABLE Cidades(
    CidadeID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    CEP TEXT NOT NULL,
    UF TEXT NOT NULL
);

CREATE TABLE UF(
    Nome_curto TEXT NOT NULL PRIMARY KEY,
    Nome_longo TEXT NOT NULL
)