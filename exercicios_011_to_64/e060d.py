# e060d.py

from keyword import kwlist


def teste(*arg,**kwargs):
    print("\nDicionario inteiro:")
    print(kwargs)
     
    print("\nItems: ")
    for x in kwargs.items():
        print (x)

    print("\nValores: ")
    for y in kwargs.values():
        print (y)

    print("\nChaves: ")
    for p in kwargs.keys():
        print (p)

teste('Rogério', 'Tatsch', 'Hanke', idade = 20, cidade = 'Floripa', uf='SC')