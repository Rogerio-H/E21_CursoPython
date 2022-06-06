# e035.py

numero = int(input("Digite um numero: "))
divisoes = 0

for i in range(1, numero + 1):
    #print(f'i ->{i} mod: {numero%i}')

    if numero %i == 0:
        divisoes += 1
        print(f'i:{i}, numero: {numero%i}, divisoes: {divisoes}')

if divisoes == 2:
    print(f'{numero} é primo!')
    print(f'{numero} é divisivel por um ou por {numero}')
else:
    print(f'{numero} não é primo')
    print(f'{numero} é divisivel { divisoes} vezes')