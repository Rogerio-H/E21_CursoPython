# e031.py

primeiro=int(input("Primeiro elemento: ") )
razao = int(input("Razao: ") )
n = 20

ultimo = primeiro + (n-1)*razao
ultimo = ultimo + 1

for i in range(primeiro, ultimo, razao):
    print(i)