# e048.py
perguntas = ["Quanto é 4 x 4",
"Quanto é 6 / 3",
]
alternativas = ["a)12\nb)24\nc)16\nd)20\n",
"a)2\nb)1\nc)3\nd)4\n"]
alternativas_certas = [{"c", "16"},
{"a", "2"}]
respostas = ["4 x 4 = 16",
"6 / 3 = 2"]

def teste():
    acertos = 0
    for pergunta, alternativa, alternativa_certa, resposta in zip(perguntas, alternativas, alternativas_certas, respostas):
        print(pergunta)
        escolha = input(alternativa).lower()
        if escolha in alternativa_certa:
            print("Acertou")
            acertos += 1
        else:
            print("Errou --->", resposta)
    print(acertos, "de", len(perguntas))

if __name__ == "__main__":
    teste()
# base = {
#     'Pergunta 01': 
#     {
#         'pergunta': 'Quanto é 4 x 4',
#         'alternativas' : {
#             'a': '12',
#             'b': '24',
#             'c': '16',
#             'd': '20'
#         },
#         'resposta_certa': 'c'
#     },
#     'Pergunta 02': {
#         'pergunta': 'Quanto é 6 / 3',
#         'alternativas': {
#             'a': '2',
#             'b': '1',
#             'c': '3',
#             'd': '4'
#         },
#         'resposta_certa': 'a'
#     },
# }

# respostas_certas = 0

# for pkeys, pvalues in base.items():
#     print(f'{pkeys}:{pvalues[ "pergunta" ]}')

#     for rkeys, rvalues in pvalues['alternativas'].items():
#         print(f'[{rkeys}]:{rvalues}')

#         resposta = input('Escolha uma alternativa: [a], [b], [c], ou [d]')
#         print('')
#         if resposta == pvalues['resposta_certa']:
#             print('Resposta Correta!')
#             respostas_certas += 1
#         else:
#             print('Resposta Errada!')

#     if respostas_certas == 0:
#         print('Voce não acertou nenhuma questão!')
#     elif respostas_certas == 1:
#         print('Você acertou apenas uma questão')
#     else:
#         print(f'Você acertou {respostas_certas}. Parabens!!!!')