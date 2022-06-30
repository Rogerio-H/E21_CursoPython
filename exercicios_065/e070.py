# e070.py
'''
70. Crie uma classe biblioteca que possui uma estrutura molde
básica para cadastro de um livro de acordo com seu titulo, 
porem que espera a inclusao de um número não definido de titulos.
Em seguida castre ao menos 5 livros nessa biblioteca. (11)
'''

class Biblioteca:
    def __init__(self, livro1):
        self.livro1 = livro1

prateleira1 = Biblioteca('1984 - George Orwell')
prateleira1.livro2 = 'A Arte da Guerra - Sun Tzu'
prateleira1.livro3 = 'Em Chamas - Suzanne Collins'

print(prateleira1.livro1)
print(prateleira1.livro2)
print(prateleira1.livro3)