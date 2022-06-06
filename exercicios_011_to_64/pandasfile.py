# pandasfile.py

import pandas as pd


'''
===================================================================================
Instalação do pandas em seu computador. Utilizar o PIP install ex.: 
    pip install pandas [enter] 
Conferir se instalou ok: 
    pip freeze 

        Deve aparecer algo assim: 
            ...
            ...
            pandas==1.4.2
            ...
            ...

observação: REINICIAR O VSCODE ... 
EXCLUAM TODOS OS TERMINAIS 
===================================================================================
'''

'''
===================================================================================
Arquivo de dados será uma planilha CSV no google Sheets ONLINE. 
Poderia ser um CSV local

Este arquivo aqui é um exemplo de configuração CSV (Tanto faz online ou local )

Url da planilha (compartilhar para o mundo)

    Clicar em:    
        Arquivo | publicar na web | pessoas (escolhar a pasta pessoas)
    Selecionar:  Planilha(aba) + formatco CSV  
    Selecionar:     republicar automaticamente quando ouver alterações [x]
    NÂO selecionar: restringer acesso [ ]


Planilha compartilhada via google sheets:
    Nome da planilha: 
        PlanilhaDadosTeste

Colunas:
id	Nome	Idade	Telefone	CEP	        Rua  	             Numero	Apto	N1	     N2	     N3	    N4

Linhas: 
1	Adriano	47	    67992636781	89010230	Rua Batman	        70		        10,20	7,50	3,20	10,20
2	Karina	45	    67992636782	89010230	Rua Capitão America	150		        10,10	7,50	3,20	10,20
3	Mario	65	    67992636783	89010230	Rua Flash	        s/n		        13,40	8,40    11,00	15,20
===================================================================================


Abaixo a URL copiada da planilha e iserida aqui dentro. 
'''
# url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS1o93qTAt7aBFyROYMLs0sAsxrhY4wwH2yABkV_wpNk6rsfY847EMFLDmZz8TVPIJKunU2G8YQkev5/pub?gid=1229205067&single=true&output=csv'
# url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS1o93qTAt7aBFyROYMLs0sAsxrhY4wwH2yABkV_wpNk6rsfY847EMFLDmZz8TVPIJKunU2G8YQkev5/pub?gid=0&single=true&output=csv'
# url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS1o93qTAt7aBFyROYMLs0sAsxrhY4wwH2yABkV_wpNk6rsfY847EMFLDmZz8TVPIJKunU2G8YQkev5/pub?gid=0&single=true&output=csv'

url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS1o93qTAt7aBFyROYMLs0sAsxrhY4wwH2yABkV_wpNk6rsfY847EMFLDmZz8TVPIJKunU2G8YQkev5/pub?gid=0&single=true&output=csv'


def importa_planilha(colunas):    
    '''Esta função retorna um DD DataDictionary direto da CSV 
    Listando a coluna ID como index pois :

    Coluna de Indice da tabela: 
    index_col=0 (representa a coluna A da planilha)

    Coluna com nomes dos campos da tabela: 
    header = 0 (represetna a Linha 1 da planilha )

    Colunas selecionadas = colunas 

    Keyword arguments:
    colunas -- Nomes das colunas (List)
    '''

    # DataFrame do Pandas --> instanciando em df 
    # df = pd.read_csv(url_or_file)
    df = pd.read_csv(url_or_file, index_col=0, header=0, usecols=colunas)



    # print(f' DataFrame: {df} ')
    
    # dd = df.to_dict('index')
    # print(df)
    # print(dd)

    # df = pd.read_csv(url_or_file, index_col=0, header=0, usecols=colunas)
    
    # df.head(3)   

    # o comando abaixo retorna para o chamador da funcao um DD Dict
    return df.to_dict('index')


# print("="*25)
# colunas = list(['id', 'Nome', 'Idade'])
# alunos = (importa_planilha(colunas))  #um dicionario de alunos vindo do google sheets 
# print(alunos)
# print("="*25)