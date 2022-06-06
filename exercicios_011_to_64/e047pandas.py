# e047pandas.py
'''
from pandasfile import importa_planilha

# Selecione o tipo de exemplo que deseja mostrar
# simples com poucas colunas (ide, nome,telefone) Imprimindo todo o conteudo
#exemplo = 
#exemplo = 2  # Simples com poucas colunas (id, nome, telefone)
exemplo = 3  # diversas colunas, e com calculo de media das clunas n1,n2,n3,n4
# Alem de mostrar as médias, cria um dicionario de dados das medias
#  com os campos: nome, média, status
print(f'Demonstração do exemplo: {exemplo}')
if (exemplo == 1):

    colunas = list(['id', 'Nome', 'Telefone'])

    # Aqui carregamos nosso DD vindo de pandasfile
    # O retorno desta função é um Dicionario de Dados importado de uma planilha CSV
    # Para chamar a função informamos quais colunas desejamos trabalhar.
    dd = importa_planilha(colunas)
     

    # Imprime todos os items
    for i in dd.items():
        print(f' Items: {i} ')

    '''     
    # Values: {
    #     'Nome': 'Adriano', 
    #     'Telefone': 67992636781
    #     } 
    # Values: {'Nome': 'Karina', 'Telefone': 67992636782} 
    # Values: {'Nome': 'Mario', 'Telefone': 67992636783} 
    # Values: {'Nome': 'Neia', 'Telefone': 67992636784} 
'''
    for i in dd.values():
        print(f' Values: {i} ')

# exemplo = 2
if (exemplo == 2 ):

    colunas = list(['id', 'Nome', 'Telefone'])

    # Aqui carregamos nosso DD vindo de pandasfile
    # O retorno desta função é um Dicionario de Dados importado de uma planilha CSV
    # Para chamar a função informamos quais colunas desejamos trabalhar.
    dd = importa_planilha(colunas)

    # Imprime todos os values
    
    '''
    ### Values: {'Nome': 'Adriano', 'Telefone': 67992636781}     
'''

    for i in dd.values():
        # Exemplo 2
        # Imprime valores de colunas selecionadas manualmente
        print(            
            i['Nome'],
            i['Telefone']
        )



if (exemplo == 3):
    novo_dic_boletim = []

    colunas = list(['id', 'Nome', 'Telefone', 'CEP','Idade', 'N1', 'N2', 'N3', 'N4'])

    # Aqui carregamos nosso DD vindo de pandasfile
    # O retorno desta função é um Dicionario de Dados importado de uma planilha CSV
    # Para chamar a função informamos quais colunas desejamos trabalhar.
    dd = importa_planilha(colunas)

    # Aqui removemos a coluna ID da lista de COLUNAS que serve apenas para informar ao dicionario
    # de dados onde está o index do CSV
    colunas.remove('id')

    print("="*60)
    for x in colunas:
        print(' ', x, end=' ')
    print("\n----------------------------------------------------------\n")


    # Aqui a chave i --> será a cada laço uma lista dos dd.values() exemplo:
# i==> {'Nome': 'Adriano', 'Telefone': 67992636781, 'CEP': 89010230, 'N1': '10,20', 'N2': '7,50', 'N3': '3,20', 'N4': '10,20'}

    for i in dd.values():
        # print(i) #bloqueado pra não poluir
        # Imprime um cabecalho na esquerda de cada linha. (i)
        print(":", end=' ')        

        # Desdobramento de i, para impressão apenas dos valores:
        # Para isto vamos usar a variavel colunas, definida acima
        # e vamos buscar por todos valores de colunas na chave i
        # N ==> Nome -->        i['Nome'] ===> Adriano
        # N ==> Telefone -->    i['Telefone'] ==> 679992636781
        # N ==> CEP -->          i['CEP'] ==> 89010230

        for N in colunas:
            print(i[N], end=' ')  
        

        # # print() não preciso mais pois o printf no final faz o pula linha LF
        # # zera contadores e somas
        soma_das_notas = 0
        numero_de_notas = 0

        # # Aqui especificamos quais são as colunas que deseamos obter a média:
        colunas_de_notas = list(['N1', 'N2', 'N3', 'N4'])

        for M in colunas_de_notas:            
            soma_das_notas += float(str(i[M]).replace(',', '.'))                      
            numero_de_notas += 1
            
            media = (soma_das_notas/numero_de_notas)
            media_arredondada = round(media, 2)
            
        print(f'Soma: {round(soma_das_notas,1)}, Média: {media_arredondada}')

        status = "Reprovado"
        if (media_arredondada>=7): 
            status = "Aprovado"

        novo_dic_boletim.append(
            {
                'Nome': i['Nome'],
                'Media': media_arredondada,
                'Status': status
            }
        )

# Ao final do imprime o boletim
    colunas_do_boletim=list(['Nome','Media','Status'])
    print("Boletim:")
    print("="*50)
    for a in colunas_do_boletim:
        print(a,end=' ')    
    
    print("\n--------------------------------------")

    # Aqui percorre o novo dict_boletim:
    # {'Nome': 'Adriano', 'Media': 5.5, 'Status': 'Reprovado'}
    # {'Nome': 'Karina', 'Media': 6.0, 'Status': 'Reprovado'}
    # {'Nome': 'Mario', 'Media': 6.0, 'Status': 'Reprovado'}


    for b in novo_dic_boletim:
        for c in colunas_do_boletim:
            print(b[c],end=' ')
        print('')
    print("======================================")
'''
from pandasfile import importa_planilha

colunas = list(['id', 'Nome', 'Idade', 'Telefone', 'CEP', 'N1'])
dd = importa_planilha(colunas)

for i in dd.items():
        print(f' Items: {i} ')




