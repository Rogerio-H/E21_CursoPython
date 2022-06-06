# e058.py

# 58. Crie uma função que pode conter dois ou mais parametros, 
# porem sem um numero definido declarado de parametros:

def funcao1(*args):
    print(f"printa tudo abaixo vvvvvvv \n{args}")

msg = funcao1(f"Pronto, printou tudo; CPF = 000.000.000-33")