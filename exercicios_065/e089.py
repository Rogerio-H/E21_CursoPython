# e089.py

from e089_dados import texto
frequencia = {}
texto = texto.lower().replace(',', "").split()

for palavra in texto:
    print('P: ', palavra)
    frequencia[palavra] = frequencia.get(palavra, 0) + 1


f2 = {}
palavras = frequencia.keys()
for i in palavras:
    print(f'{i} = {frequencia[i]}')

alfa = sorted(palavras)
print(alfa)