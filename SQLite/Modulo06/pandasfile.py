import pandas as pd


url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSp3N0iSajaKoFaRiiTOV1Qxm1Y6-_B1IKJsKaqjiBhJbNIrjER4Kr2YtDHn8xNsFvWhQiGBK-Q5MQN/pub?gid=0&single=true&output=csv'

colunas = list(['id','UF','Município'])

df = pd.read_csv(url_or_file, index_col=0, header=0, usecols=colunas)

print(df)