# e042.py
texto = 'Python é uma linguagem de programação de alto nível'
frase = str(texto).strip().upper()
palavras = frase.split()
nomes = palavras
print(nomes)

nomes.append('trevas')
# print(nomes)

nomes.insert(1, 'NÃO')
# print(nomes)
# print(palavras) 

nomes.remove('PYTHON')
print("Nomes ..:", nomes)