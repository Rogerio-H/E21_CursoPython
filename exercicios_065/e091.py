# e091.py
# Escreva um programa da forma mais reduzida possível, que recebe do usuário uma série de nomes, 
# separando os mesmos e os organizando em ordem alfabética. Em Seguida exiba em tela os nomes já ordenados.

nomes = str(input('Digite 5 nomes: ')).split()
print(sorted(nomes))