# e055b.py

def boas_vindas(nome,sobrenome):
    print(f'Seja bem vindo: {nome} {sobrenome}')
    

nome = str(input('Digite nome:')).lower()
sobrenome = str(input('Digite sobrenome:')).lower()

pessoa = boas_vindas(nome,sobrenome)