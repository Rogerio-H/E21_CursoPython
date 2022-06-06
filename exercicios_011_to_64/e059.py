# e059.py

# 59. Crie uma função de numero de parametros indefinido, 
# que realiza a soma dos números repassados como parâmetro, 
# independentemente da quantidade de números:
 
def soma_todos(*args):
    print(args)
    print(type(args))

    num = 0
    for x in args:
        num += x

    print(f"A soma é {num}")

soma = soma_todos(10, 20, 30, 40, 50)