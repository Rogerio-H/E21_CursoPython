# e062.py

# 62. Crie um programa modularizado, onde em um arquivo teremos uma lista de médicos ficticios 
# a serem consultados, em outro arquivo, teremos a estrutura principal do programa, que por 
# sua vez realiza o agendamento de uma consulta médica com base na interação com o usuário.

from medicos import medico

while True:
    print(f"\033[1;31;40mLista de médicos:\n \033[0;37;40m")

    for k, v in medico.items():
        print(f'{k}:\n - {v}')
    
    agend = input('\nDigite o nome do médico que gostaria de ser atendido: ').title()
    
    if medico.get(agend):
        print(f'\nConsulta agendada com: {medico[agend]}')
        break
    else:
        print("\nMédico não existente, tente novamente\n")
        