# e060c.py

def teste(*arg, idade = 45):
    for x in arg:
        print(str(x).lower())
    print(idade)

teste('Rogério', 'Tatsch', 'Hanke', idade = 20)