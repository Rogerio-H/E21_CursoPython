

BEGIN TRANSACTION;

DROP TABLE IF EXISTS PRODUTOS;

CREATE TABLE PRODUTOS(
    PRODUTOS_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    PRODUTOS_NOME TEXT NOT NULL,
    PRODUTOS_VALOR TEXT NOT NULL,
    PRODUTOS_LOCAL INTEGER 
);

DROP TABLE IF EXISTS ATENDENTES;

CREATE TABLE ATENDENTES(
    ATENDENTES_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ATENDENTES_NOME TEXT NOT NULL
);

DROP TABLE IF EXISTS CLIENTES;

CREATE TABLE CLIENTES(
    CLIENTES_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    CLIENTES_NOME TEXT NOT NULL,
    CLIENTES_FONE TEXT NOT NULL,
    CLIENTES_CPF INTEGER,
    CLIENTES_TOTALDECOMPRAS INTEGER --ITENS_VALORTOTAL
);

DROP TABLE IF EXISTS PRATELEIRAS;

CREATE TABLE PRATELEIRAS(
    PRATELEIRAS_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    PRATELEIRAS_NOME TEXT NOT NULL,
    PRATELEIRAS_LOCAL TEXT NOT NULL
);

DROP TABLE IF EXISTS ITENS_NOTA;

CREATE TABLE ITENS_NOTA(
    ITENS_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ITENS_SEQUENCIA INTEGER,
    ITENS_PRODUTO TEXT NOT NULL, --PRODUTOS_NOME_ID
    ITENS_NUMERONOTA INTEGER,
    ITENS_QUANTIDADE INTEGER,
    ITENS_VALORUNID TEXT NOT NULL,
    ITENS_VALORTOTAL TEXT NOT NULL
);

DROP TABLE IF EXISTS NOTA_FISCAL;

CREATE TABLE NOTA_FISCAL( 
    NOTA_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOTA_DATA DATETIME DEFAULT CURRENT_TIMESTAMP,
    NOTA_NUM INTEGER,
    NOTA_CLIENTES INTEGER, --CLIENTES_ID
    NOTA_ATENDENTES INTEGER --ATENDENTES_ID
);

COMMIT;

INSERT INTO ATENDENTES (ATENDENTES_NOME)
    VALUES
    ('Dorivaldo'),
    ('Wesley'),
    ('Samira'),
    ('Leonardo'),
    ('Edenilson'),
    ('Carla'),
    ('Laura'),
    ('Hugo'),
    ('Mauricio'),
    ('Ronaldo');


INSERT INTO PRODUTOS (PRODUTOS_NOME, PRODUTOS_VALOR, PRODUTOS_LOCAL)
    VALUES
    ('Refrigerante Cola', 'R$22,00', '10'),
    ('Refrigerante Guarana', 'R$29,50', 10),
    ('Refrigerante Laranja', 'R$28,00', 10),
    ('Refrigerante Abacaxi', 'R$1,00', 10),
    ('Refrigerante Limão', 'R$1,00', 10),
    ('Vinho Tinto Seco', 'R$16,00', 10),
    ('Vinho Tinto Suave', 'R$14,50', 10),
    ('Vinho Branco Seco', 'R$23,50', 10),
    ('Vinho Branco Suave', 'R$5,50', 10),
    ('Vinho de Pessego', 'R$1,00', 10),
    ('Bitter', 'R$10,00', 10),
    ('Vermuth Tinto', 'R$13,00', 10),
    ('Vermuth Branco', 'R$16,00', 10),
    ('Vodka Orloff', 'R$29,50', 10),
    ('Vodka Smirnoff', 'R$15,60', 10),
    ('Whisky red Label','R$ 16,00',10),
    ('Whisky Black Label','R$ 8,50',10),
    ('Velho Barreiro','R$ 4,00',10),
    ('Cerveja Bhrama 600Ml','R$ 10,00',10),
    ('Cerveja Bhrama lata','R$ 5,60',10),
    ('Cerveja Skol 600Ml','R$ 2,30',10),
    ('Cerveja Skol lata','R$ 22,00',10),
    ('Cerveja Bohemia 600Ml','R$ 7,00',10),
    ('Cerveja Bohemia Lata','R$ 29,90',10),
    ('Cerveja Stella 200Ml','R$ 20,00',10),
    ('Cerveja Stella Lata','R$ 7,30',10),
    ('Cerveja Quilmes 1L','R$ 21,20',10),
    ('Cerveja Patricia 1L','R$ 11,00',10),
    ('Cerveja Budwieser Lata','R$ 23,80',10),
    ('Cerveja Original 600Ml','R$ 26,50',10),
    ('Cerveja Corona 300ML','R$ 4,00',10),
    ('Cerveja caracu Preta lata','R$ 23,50',10),
    ('Cerveja Caracu Long Neck','R$ 8,60',10),
    ('Cerveja Heineken 330ml','R$ 23,00',10),
    ('Cerveja Heineken 600ml','R$ 9,00',10),
    ('Bala Suspense  700g','R$ 5,70',2),
    ('Bala de Banana 700g','R$ 15,80',2),
    ('Bala Cereja 700g','R$ 3,40',2),
    ('Bala Azedinha 700g','R$ 20,20',2),
    ('Choc. Prestigio Cx16','R$ 14,80',2),
    ('Choc. Sensação Cx16','R$ 1,00',2),
    ('Choc. Chokito Cx16','R$ 26,00',2),
    ('Choc. Suflair Cx16','R$ 12,00',2),
    ('Choc. Charge Cx16','R$ 17,00',2),
    ('Bombom Sonho de valsa 1kg','R$ 14,00',2),
    ('Bombom Ouro Branco 1KG','R$ 3,50',2),
    ('Salgadinho Bacon 70Gr','R$ 6,50',1),
    ('Salgadinho Pizza 70Gr','R$ 8,90',1),
    ('Salgadinho Cebola 70Gr','R$ 20,00',1),
    ('Salgadinho Queijo 70Gr','R$ 21,00',1),
    ('Pipoca Doce','R$ 28,00',1),
    ('Pipoca Salgada','R$ 27,50',1),
    ('Paçoca Santa Helena 110Un','R$ 23,60',2),
    ('Paçoca Santa Helena 65Un','R$ 21,30',2),
    ('Amendoim S/Pele','R$ 19,00',3),
    ('Amendoim C/Pele','R$ 16,00',3),
    ('Amendoim Japones','R$ 13,20',3),
    ('Amendoim C/ Chocolate','R$ 14,99',3),
    ('Amendoim Pasta Integral 500g','R$ 1,00',3),
    ('Bolacha recheada Morango 90g','R$ 2,65',7),
    ('Bolacha recheada Chocolate 90g','R$ 1,99',7),
    ('Bolacha recheada Limao 90g','R$ 4,68',7),
    ('Bolacha recheada Creme 90g','R$ 22,00',7),
    ('Bolacha Cream Craker 110G','R$ 1,00',7),
    ('Bolacha Salgada 110G','R$ 13,86',7),
    ('Bolacha Amanteigada 110G','R$ 22,00',7),
    ('Bolacha Amendoim 110g','R$ 7,45',7),
    ('Bolacha de Coco 110','R$ 9,32',7),
    ('Bolacha de Milho 110g','R$ 4,99',7),
    ('Sabão em PO ','R$ 3,99',5),
    ('Sabao Liquido','R$ 13,00',5),
    ('Agua Sanitaria 5L','R$ 7,00',5),
    ('Amaciante 5L','R$ 10,00',5),
    ('Desinfetante 5L','R$ 10,00',5),
    ('Detergente Liquido 5L','R$ 1,00',5),
    ('Papel Higienico 24UN','R$ 25,00',5),
    ('Papel Higienico 12Un','R$ 2,89',5),
    ('Papel Higienico 48UN','R$ 6,79',5),
    ('Toalha Papel 1000UN','R$ 16,00',5),
    ('Papel Toalha C/4','R$ 4,32',5),
    ('Guardanapo C 24Un','R$ 22,00',5),
    ('Guardanapo CX','R$ 6,23',5),
    ('Filtro de cafe CX 100UN','R$ 7,89',1),
    ('Arroz 1Kg','R$ 14,37',1),
    ('Arroz 5K','R$ 4,00',1),
    ('Feijao Branco 1K','R$ 16,85',1),
    ('Feijao Preto 1K','R$ 17,32',1),
    ('Feijao carioquinha 1K','R$ 19,00',1),
    ('Macarrao Espaguete 500GR','R$ 1,00',10),
    ('Macarrao Pene 500GR','R$ 1,99',10),
    ('Macarrao 500GR','R$ 23,50',10),
    ('Oleo de Oliva 750ML','R$ 14,50',9),
    ('Azeite 900ML','R$ 26,67',9),
    ('Tempero Completo 200Gr','R$ 5,32',9),
    ('Tempero Completo C Pimenta 200Gr','R$ 20,49',9),
    ('Maionese 500GR','R$ 12,52',8),
    ('Maionese 200Gr','R$ 16,82',8),
    ('Margarina 400GR','R$ 1,62',8),
    ('Margarina 150GR','R$ 25,00',8),
    ('Extrato de tomate 90GR','R$ 16,80',8),
    ('Extrato de tomate 45GR','R$ 20,30',8),
    ('Atum ','R$ 23,30',1),
    ('Sardinha','R$ 29,99',1),
    ('Milho Ervilha ','R$ 30,99',1),
    ('Milho ','R$ 2,65',1),
    ('Ervilha','R$ 4,99',1),
    ('Salsicha enlatada','R$ 3,99',1),
    ('Salsicha de Frango ','R$ 0,99',1),
    ('Farofa C/ Pimenta 90GR','R$ 3,56',1),
    ('Farofa Churrasco 90GR','R$ 10,00',1),
    ('Farofa Tradicional 90Gr','R$ 8,60',1),
    ('Farofa Costela 90Gr','R$ 19,00',1),
    ('Farinha doce 1K','R$ 5,60',6),
    ('Farinha Azeda 1K','R$ 16,00',6),
    ('Cafe Tradicional 500G','R$ 8,99',6),
    ('Cafe Extra Forte 500G','R$ 7,99',6),
    ('Cafe em capsula CX 16','R$ 21,99',6),
    ('Leite 1L Integral','R$ 1,00',6),
    ('Leite 1L Desnatado','R$ 8,55',6),
    ('Leite 1L Semi Desnatado','R$ 28,00',6),
    ('Achocolatado 1L ','R$ 28,00',7),
    ('Achocolatado PO 400Gr','R$ 22,00',7),
    ('Cha de Erva Doce 90Gr','R$ 19,00',7),
    ('Cha Cascara Sagrada 90G','R$ 22,00',7),
    ('Cha Hortela 90g','R$ 14,36',7),
    ('Cha Verde 90G','R$ 1,00',7),
    ('Cha Preto 90G','R$ 1,00',7),
    ('Cha Carqueja 90G','R$ 25,00',7),
    ('Fruta Uva 500Gr','R$ 19,00',8),
    ('Fruta Abacaxi UN','R$ 25,00',8),
    ('Fruta Laranja 500Gr','R$ 26,99',8),
    ('Fruta Morango Bandeja','R$ 19,00',8),
    ('Fruta Melancia Un','R$ 1,56',8),
    ('Fruta Maça 500GR','R$ 7,00',8),
    ('Fruta Acerola 500Gr','R$ 4,00',8),
    ('Fruta Jabuticaba 500Gr','R$ 25,00',8),
    ('Fruta Goiaba 500Gr','R$ 23,96',8),
    ('Carne Picanha KG','R$ 11,99',9),
    ('Carne Maminha KG','R$ 20,50',9),
    ('Carne Contra File KG','R$ 10,00',9),
    ('Carne Costela KG','R$ 11,50',9),
    ('Carne Fraldinha KG','R$ 6,89',9),
    ('Carne Cochão Duro KG','R$ 10,00',9),
    ('carne Cochão Mole KG','R$ 25,00',9),
    ('Carne Cupim KG','R$ 13,00',9),
    ('Carne Contra File KG','R$ 13,00',9),
    ('Carne Moida KG','R$ 5,69',9),
    ('Carne de Porco Lombo Kg','R$ 19,00',9),
    ('Carne de porco Costela KG','R$ 13,00',9),
    ('Peixe Tilapia KG','R$ 18,32',9),
    ('Peixe File 500GR','R$ 25,00',9),
    ('Peixe Tainha KG','R$ 21,99',9),
    ('Peixe Salmao KG','R$ 23,90',9),
    ('Salame de frango KG','R$ 1,00',9),
    ('Salame Misto KG','R$ 7,00',9),
    ('Salame de Porco KG','R$ 11,26',9),
    ('Carvão 3Kg','R$ 28,00',9),
    ('Carvão 5Kg','R$ 22,00',9),
    ('Creme de leite Lt','R$ 28,00',6),
    ('Leite Condensado LT','R$ 25,00',6),
    ('Vinagre','R$ 7,00',1),
    ('Alcool','R$ 5,50',1),
    ('Amido de milho','R$ 20,50',1),
    ('Fermento','R$ 17,50',3),
    ('Sal','R$ 13,00',3),
    ('Farinha de trigo','R$ 1,00',3),
    ('Farinha de milho','R$ 7,00',3),
    ('Gelatina Morango','R$ 5,50',3),
    ('Gelatina Abacaxi','R$ 13,00',2),
    ('Gelatina Limão','R$ 8,99',2),
    ('Gelatina Framboesa','R$ 26,99',2),
    ('Gelatina Laranja','R$ 28,00',2),
    ('Cereal de Flocos','R$ 7,00',4),
    ('Cereal Achocolatado','R$ 12,99',4),
    ('Torrada tradiocinal 100Gr','R$ 19,00',4),
    ('Torrada Integral 100Gr','R$ 8,99',4),
    ('Torrada de cebola e salça 100Gr','R$ 21,99',4),
    ('Ovos 12Un','R$ 10,00',9),
    ('Ovos 30Un','R$ 4,00',9),
    ('Ovos caipira 18Un','R$ 6,99',9),
    ('Shampoo','R$ 13,98',4),
    ('Condicionador','R$ 21,89',4),
    ('Creme para pentear','R$ 14,91',4),
    ('Sabonete ','R$ 13,95',4),
    ('Creme dental','R$ 2,65',4),
    ('Escova de dente','R$ 7,00',4),
    ('Hidratante Corporal','R$ 7,32',4),
    ('Fralda P','R$ 3,65',4),
    ('Fralda M','R$ 8,56',4),
    ('Fralda G','R$ 16,00',4),
    ('Fralda GG','R$ 28,00',4),
    ('Lenço Umidecido','R$ 7,62',4),
    ('Lamina de Barbear','R$ 9,21',4),
    ('Esmalte para unhas','R$ 1,58',4),
    ('Aparador de pontas','R$ 2,67',4),
    ('Alicate de Unha','R$ 3,94',4),
    ('hidratante para o rosto','R$ 1,00',4),
    ('Hidratante pos barba','R$ 10,00',4),
    ('Hidratante para barbear','R$ 28,00',4),
    ('Escova de Cabelo','R$ 3,68',4);

INSERT INTO PRATELEIRAS (PRATELEIRAS_NOME, PRATELEIRAS_LOCAL)
    VALUES
    ('Salgados', 'corredor 1'),
    ('Doces', 'corredor 2'),
    ('Frios ', 'corredor 3'),
    ('Higiene e beleza', 'corredor 4'),
    ('Limpeza', 'corredor 5'),
    ('Latcinios ', 'corredor 6'),
    ('Biscoitos', 'corredor 7'),
    ('Hortifruti ', 'corredor 8'),
    ('Carnes', 'corredor 9'),
    ('Bebidas', 'corredor 10');

INSERT INTO CLIENTES (CLIENTES_NOME, CLIENTES_FONE, CLIENTES_CPF, CLIENTES_TOTALDECOMPRAS)
    VALUES
    ('Olga Hanke','94 92859-4273',94276558018,'R$ 1.377.45'),
    ('Otavio de Souza','92 93979-3586',47226202026,'R$ 1.063.34'),
    ('Otto Silva','81 92376-7315',13979821013,'R$ 1.833.52'),
    ('Paulo Silva','82 93732-1545',70949758051,'R$ 1.833.52'),
    ('Poliana Cardoso','95 93857-4843',40696450046,'R$ 1.394.76'),
    ('Raissa Veiga','38 93871-3644',29349184087,'R$ 2.345.34'),
    ('Rodrigo Borges','53 93255-1021',6369400041,'R$ 956.40'),
    ('Romario Nardino','16 93456-8524',26065962007,'R$ 1.078.18'),
    ('Sabrina Costa','96 92670-8284',45872525060,'R$ 2.286.87'),
    ('Salete Maros','94 92194-4797',47962658053,'R$ 1.858.76'),
    ('Sarah Moraes','97 93000-3184',33247045023,'R$ 2.390.42'),
    ('Saulo Bitencourt','63 93615-7772',44133574001,'R$ 2.451.18'),
    ('Sergio Pinto','63 92815-8797',69396344010,'R$ 1.387.49'),
    ('Sheila Nardino','95 92982-8536',13696551007,'R$ 958.43'),
    ('Silvane Drosdek','53 92864-1168',37820621087,'R$ 2.763.41'),
    ('Silvio Dutra','54 92684-3474',28033293012,'R$ 2.537.21'),
    ('Sonia Hanke','55 92128-6188',39742890030,'R$ 1.514.40'),
    ('Soraya Dimas','53 93493-2665',51932900004,'R$ 2.289.73'),
    ('Tatiana Salomon','51 93226-4911',15342078059,'R$ 2.426.49'),
    ('Teodoro Veiss','55 93689-6837',65642186051,'R$ 2.894.43'),
    ('Teresa Nascimento','54 92857-8896',91748328085,'R$ 2.539.82'),
    ('Tobias Campos','55 92126-6584',35332994060,'R$ 1.945.63'),
    ('Valdemar Pereira','53 92857-2900',75478692034,'R$ 2.478.63'),
    ('Valentim Duarte','53 93238-0303',18935942030,'R$ 2.003.80'),
    ('Valeria Gomes','98 93311-5124',17913255056,'R$ 3.222.91'),
    ('Vanessa Lima','8393442-8328',87372224063,'R$ 2.105.98'),
    ('Vitor Velasques','82 92835-6081',26442615030,'R$ 1.975.43'),
    ('Vitoria Garcia','55 92151-5131',97976329030,'R$ 2.197.40'),
    ('Viviane Cardoso','94 92815-8833',1085424081,'R$ 2.273.42'),
    ('Zuleide Lopes','53 93081-2382',84775185055,'R$ 2.078.81');

INSERT INTO NOTA_FISCAL(NOTA_DATA, NOTA_NUM, NOTA_CLIENTES, NOTA_ATENDENTES)
    VALUES
    ('01/01/2022',1,70,10),
    ('02/01/2022',2,71,9),
    ('03/01/2022',3,72,8),
    ('04/01/2022',4,73,7),
    ('05/01/2022',5,74,6),
    ('06/01/2022',6,75,5),
    ('07/01/2022',7,76,4),
    ('08/01/2022',8,77,3),
    ('09/01/2022',9,78,2),
    ('10/01/2022',10,79,1),
    ('11/01/2022',11,80,10),
    ('12/01/2022',12,81,9),
    ('01/01/2023',13,82,8),
    ('02/01/2023',14,83,7),
    ('03/01/2023',15,84,6),
    ('04/01/2023',16,85,5),
    ('05/01/2023',17,86,4),
    ('06/01/2023',18,87,3),
    ('07/01/2023',19,88,2),
    ('08/01/2023',20,89,1),
    ('09/01/2023',21,90,10),
    ('10/01/2023',22,91,9),
    ('11/01/2023',23,92,8),
    ('12/01/2023',24,93,7),
    ('01/01/2024',25,94,6),
    ('02/01/2024',26,95,5),
    ('03/01/2024',27,96,4),
    ('04/01/2024',28,97,3),
    ('05/01/2024',29,98,2),
    ('06/01/2024',30,99,1);

INSERT INTO ITENS_NOTA(ITENS_SEQUENCIA, ITENS_PRODUTO, ITENS_NUMERONOTA, ITENS_QUANTIDADE, ITENS_VALORUNID, ITENS_VALORTOTAL)
    VALUES
    (1000,1,1,1,22,22),
    (1001,2,1,1,29.5,29.5),
    (1002,27,1,1,21.2,21.2),
    (1003,28,1,6,11,66),
    (1004,29,1,6,23.8,142.8),
    (1005,30,1,6,26.5,159),
    (1006,41,1,2,1,2),
    (1007,42,1,1,26,26),
    (1008,43,1,2,12,24),
    (1009,44,1,4,17,68),
    (1010,55,1,2,19,38),
    (1011,56,1,2,16,32),
    (1012,57,1,3,11,33),
    (1013,58,1,1,9,9),
    (1014,85,1,3,4,12),
    (1015,86,1,2,16.85,33.7),
    (1016,87,1,4,17.32,69.28),
    (1017,88,1,2,19,38),
    (1018,112,1,4,19,76),
    (1019,113,1,2,5.6,11.2),
    (1020,114,1,1,16,16),
    (1021,115,1,5,8.99,44.95),
    (1022,135,1,4,4,16),
    (1023,136,1,2,25,50),
    (1024,137,1,2,23.96,47.92),
    (1025,138,1,10,11.99,119.9),
    (1026,159,1,2,28,56),
    (1027,160,1,2,25,50),
    (1028,161,1,6,7,42),
    (1029,162,1,4,5.5,22),
--------------------------------------------------
    (1000,184,2,6,13.95,83.7),
    (1001,185,2,5,2.65,13.25),
    (1002,186,2,3,7,21),
    (1003,187,2,7,7.32,51.24),
    (1004,188,2,15,3.65,25.55),
    (1005,189,2,6,8.56,51.36),
    (1006,190,2,4,16,64),
    (1007,191,2,1,28,28),
    (1008,192,2,10,7.62,76.2),
    (1009,193,2,4,9.21,36.84),
    (1010,194,2,8,1.58,12.64),
    (1011,195,2,2,2.67,5.34),
    (1012,196,2,1,3.94,3.94),
    (1013,197,2,5,1,5),
    (1014,198,2,1,10,10),
    (1015,199,2,1,28,28),
    (1016,200,2,4,3.68,14.72),
    (1017,129,2,2,19,38),
    (1018,130,2,1,25,25),
    (1019,131,2,2,26.99,53.98),
    (1020,132,2,3,19,57),
    (1021,133,2,5,1.56,7.8),
    (1022,134,2,1,7,7),
    (1023,135,2,2,4,8),
    (1024,136,2,3,25,75),
    (1025,137,2,5,23.96,119.8),
    (1026,138,2,2,11.99,23.98),
    (1027,139,2,2,20.5,41),
    (1028,140,2,3,10,30),
    (1029,141,2,4,11.5,46),
    
    
    (1000,184,2,6,13.95,83.7),
    (1001,185,2,5,2.65,13.25),
    (1002,186,2,3,7,21),
    (1003,187,2,7,7.32,51.24),
    (1004,188,2,15,3.65,25.55),
    (1005,189,2,6,8.56,51.36),
    (1006,190,2,4,16,64),
    (1007,191,2,1,28,28),
    (1008,192,2,10,7.62,76.2),
    (1009,193,2,4,9.21,36.84),
    (1010,194,2,8,1.58,12.64),
    (1011,195,2,2,2.67,5.34),
    (1012,196,2,1,3.94,3.94),
    (1013,197,2,5,1,5),
    (1014,198,2,1,10,10),
    (1015,199,2,1,28,28),
    (1016,200,2,4,3.68,14.72),
    (1017,129,2,2,19,38),
    (1018,130,2,1,25,25),
    (1019,131,2,2,26.99,53.98),
    (1020,132,2,3,19,57),
    (1021,133,2,5,1.56,7.8),
    (1022,134,2,1,7,7),
    (1023,135,2,2,4,8),
    (1024,136,2,3,25,75),
    (1025,137,2,5,23.96,119.8),
    (1026,138,2,2,11.99,23.98),
    (1027,139,2,2,20.5,41),
    (1028,140,2,3,10,30),
    (1029,141,2,4,11.5,46);
