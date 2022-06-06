# e60e.py

def teste (*arg, **kwargs):
    print('='*20)
    for a in arg:
        print(f'argumento(s): {a}')
    
    for k, v in kwargs.items():
        print(f' parametro(s): {k}, {v}')

teste('Rogério', idade = 20, cidade = 'Floripa')