import pandas as pd
import sqlite3 


cnx = sqlite3.connect('e2002.sqlite3')
cur = cnx.cursor()



url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSp3N0iSajaKoFaRiiTOV1Qxm1Y6-_B1IKJsKaqjiBhJbNIrjER4Kr2YtDHn8xNsFvWhQiGBK-Q5MQN/pub?gid=0&single=true&output=csv'

colunas = list(['id','UF','Município'])

df = pd.read_csv(url_or_file, index_col=0, header=0, usecols=colunas)
# df.to_sql('CIDADES', cnx, if_exists='replace', index = False)

cur.execute("""
    DROP TABLE IF EXISTS CIDADES;
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS CIDADES(
        id INTEGER PRIMARY KEY,
        UF TEXT NOT NULL,
        Município TEXT NOT NULL
    );
""")

df.to_sql('CIDADES', cnx, if_exists='replace', index = False)
# sql = ("INSERT INTO CIDADES (UF, Município) VALUES(?, ?), row['UF'], row['Município']")

cur.execute("INSERT INTO CIDADES (UF, Município) VALUES(?, ?), row['UF'], row['Município']")
cnx.commit()

cur.execute(""" 
    SELECT * FROM CIDADES;
""")

