# e063.py
# 63. Aprimore o exemplo anterior, incluindo um módulo simulando o cadastro de usuarios 
# em um plano de saude, apenas permitindo o agendamento da consulta caso o usuário que está interagindo com o programa conste no cadastro:
#  1.  Exercicios para fixação opcional
#    1.  Modularize as verificações de usuario. (ou crie uma função para limpar o main ao maximo)
#    2.  Modularize as escolha de médico. (ou crie uma função)         3.  
#    4.  Remova todas as constantes do programa utilizando os dados dos modulos para imprimir e testar.

#===============Não está feito================

from medicos import medico

while True:
    print(f"\033[1;31;40mLista de médicos:\n \033[0;37;40m")

    for k, v in medico.items():
        print(f'{k}:\n - {v}\n')

    agend = input('\nDigite o nome do médico que gostaria de ser atendido: ').title()
    if medico.get(agend):
        print(f'\nConsulta agendada com: {medico[agend]}')
        break
    else:
        print("\nMédico não existente, tente novamente\n")