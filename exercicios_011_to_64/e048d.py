# e048d.py

lista = ([
    [10, 20, [30, 33]],
    [40, 50, [60, 65]],
    [70, 80, [90, 95]]
    ])
for a, b, c in lista:
    print('a: ', (a*a))
    print('b: ', (b*b))
    print('c: ', c)
    soma = 0
    for x in list(c):
        soma = soma + x
    print(soma)
