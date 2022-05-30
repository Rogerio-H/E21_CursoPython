# e047b.py

from modulo import situacao


def media(aluno):
    # print(aluno)
    boletim = []

    for i in aluno:
        media_r = round(sum(i['Notas'])/len(i['Notas']), 1),
        
        boletim.append(
        {
            'Nome' : i['Nome'],
            'Media de Notas' : media_r,
            'Boletim': situacao
        }
    )
    return boletim

aluno = [
    {
        'Nome': 'Adriano',
        'Notas': [7.7, 7.0, 6.9]  
    },
    {
        'Nome': 'rogerio',
        'Notas': [9.0, 7.0, 4.8]
    }
    ]

blt = media(aluno)
print(blt)