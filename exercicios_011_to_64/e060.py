# e060.py

def id(*args, **kwargs):

    for n in args: 
        nome = n
        print(f'{n}')

        for k, v in kwargs.items():
            idade = k
            sexo = v
            print(f'{idade}, {sexo}')

id('Rogério', idade = '20', sexo = 'Masculino')
