# e040.py

texto = 'Python é uma linguagem de programação de alto nível'
frase = str(texto).strip().upper()
palavras = frase.split()
nomes = palavras
print(nomes)

nomes.append('trevas')
print(nomes)