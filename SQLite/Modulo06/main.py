import sqlite3 

cnx = sqlite3.connect('modulo06.sqlite3')
cur = cnx.cursor()

cur.execute("""
    DROP TABLE IF EXISTS CIDADES;
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS CIDADES(
        CIDADE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CIDADE_NOME TEXT NOT NULL
    );
""")

cur.execute("""
    DROP TABLE IF EXISTS PESSOAS;
""")

cur.execute("""
    CREATE TABLE PESSOAS(
        PESSOAS_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PESSOAS_NOME TEXT NOT NULL,
        PESSOAS_IDADE INTEGER,
        PESSOAS_CIDADES_ID INTEGER NOT NULL
);

""")
cur.execute("""
    INSERT INTO CIDADES(CIDADE_NOME) VALUES
    ('RIO NEGRINHO'),
    ('FLORIPA'),
    ('JOINVILLE'),
    ('PORTO ALEGRE');
""")

cnx.commit()

cur.execute("""
    INSERT INTO PESSOAS(PESSOAS_NOME, PESSOAS_IDADE, PESSOAS_CIDADES_ID)
        VALUES
        ('Rogério Hanke', 20, 2),
        ('Marina', 21, 4),
        ('Jéssica', 22, 1);
""")

cnx.commit()

# Fetchone()

# cur.execute("SELECT * FROM CIDADES;")
# primeiro_resultado = cur.fetchone()
# print(f'\nPrimeira Linha: {primeiro_resultado}')

#Fetchmany()

# cur.execute("SELECT * FROM CIDADES;")
# dois_resultados = cur.fetchmany(2)
# print(f'\nPrimeira Linha: {dois_resultados}')

#Fetchall()

# cur.execute("SELECT * FROM CIDADES;")
# todos_resultados = cur.fetchall()
# print(f'\nPrimeira Linha: {todos_resultados}')

cur.execute(""" 
    SELECT PESSOAS_NOME, CIDADE_NOME FROM PESSOAS, CIDADES
        WHERE PESSOAS_CIDADES_ID = CIDADE_ID;
""")
todos_resultados = cur.fetchall()
print(f'\nPrimeira Linha: {todos_resultados}')