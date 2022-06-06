# e057.py

#  57 Crie uma função com tres parametros, sendo dois
#  deles com dados/valores padrão, alterando o terceiro deles
#  contornando o paradigma da justaposição de argumentos. 

def console1(console, lancamento = 2014, empresa = 'Microsoft'):
    print(f'{console} lancou em {lancamento} e é da {empresa}')

c1 = console1('Playstation4', empresa='Sony')