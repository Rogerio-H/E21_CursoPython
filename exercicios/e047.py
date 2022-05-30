# e047.py


def media(aluno):
    # print(aluno)
    boletim = []

    for i in aluno:
        boletim.append(
        {
            'Nome' : i['Nome'],
            'Media de Notas' : round(sum(i['Notas'])/len(i['Notas']), 1),
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