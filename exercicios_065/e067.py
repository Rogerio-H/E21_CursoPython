# e067.py

class Carro:
    ano = 2022
    cor = 'Cinza'
    modelo = 'Sedan'

carro1 = Carro()

carro2 = Carro()
carro2.ano = 2021
carro2.cor = 'Vermelho'

print(f'=='*10)
print(carro1.ano)
print(carro1.cor)
print(carro1.modelo)
print(f'=='*10)
print(carro2.ano)
print(carro2.cor)
print(carro2.modelo)
print(f'=='*10)