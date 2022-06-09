# epandascopa.py

from pandasfilecopa import importa_planilha

colunas = list(['País', 'Títulos Copa', 'População(2020)'])
dd = importa_planilha(colunas)


# for i in dd.keys():
#         print(f' {i}: ')

for k in dd.keys():
        # for x in dd.values():
        #         print(f' {x}: {k}')
        print('=='*25)
        print(k, dd[k])

# for x in dd.values():
#         print(x)

#fazer algumas alteraçoes dps (values) etc etc