# epandascopa.py

from pandasfilecopa import importa_planilha

colunas = list(['País', 'Títulos Copa', 'População(2020)'])
dd = importa_planilha(colunas)

for i in dd.items():
        print(f' Items: {i} ')

#fazer algumas alteraçoes dps (values) etc etc