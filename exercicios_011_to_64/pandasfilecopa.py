# pandasfilecopa.py

import pandas as pd

url_or_file = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQ8_9vtqX3lxo99B-tf7VdcmdbKiCkI2U8avjhwVR2yynceZ03V0p4HlLyUf57PYpN7vHYhH_Av1Z5t/pub?gid=0&single=true&output=csv'

def importa_planilha(colunas):

    df = pd.read_csv(url_or_file, index_col=0, header=0, usecols=colunas)
    return df.to_dict('index')