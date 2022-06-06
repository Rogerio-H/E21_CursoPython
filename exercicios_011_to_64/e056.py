# e056.py

def boas_vindas(nome, nacionalidade= "Argentino"):
    print(f'Olá {nome} você é {nacionalidade}')

nome = input("Digite seu nome: ")
ex1 = boas_vindas(nome)

nac = input("Digite sua nacionalidade: ")
ex2 = boas_vindas(nome, nac)