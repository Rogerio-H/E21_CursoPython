import sqlite3 

cnx = sqlite3.connect('modulo06.sqlite3')
cur = cnx.cursor()

cur.execute("SELECT * FROM CIDADES;")
todos_resultados = cur.fetchall()
# print(f'\nTodos: {todos_resultados}')
# print(type(todos_resultados))
for x, y in todos_resultados:
    print(f'{x}:{y}')

cur.execute("SELECT * FROM PESSOAS;")
todos_resultados = cur.fetchall()
for x, y, w, z in todos_resultados:
    print(f'{x}:{y}:{w}:{z}')