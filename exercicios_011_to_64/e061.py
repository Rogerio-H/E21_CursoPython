# e061.py
# 61. Escreva um programa que retorna o numero Fibonacci: sendo
# o numero de Fibonacci um valor iniciado em 0 ou em 1 onde 
# cada termo subsequente corresponde a soma dos dois anteriores.

n = int(input("quantos termos: "))
ultimo = 1
penultimo = 1

if(n==1) or (n==2):
    print('é 1 mesmo')
else: 
    for i in range(2,n):
        fibo = ultimo + penultimo
        penultimo = ultimo
        ultimo = fibo
        i += 1
    print(fibo)