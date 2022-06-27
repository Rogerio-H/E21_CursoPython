# e062.py

# 62. Crie um programa modularizado, onde em um arquivo teremos uma lista de médicos ficticios 
# a serem consultados, em outro arquivo, teremos a estrutura principal do programa, que por 
# sua vez realiza o agendamento de uma consulta médica com base na interação com o usuário.

from medicos import medico

while True:
    print(f"\033[1;31;40m\tLista de médicos:\n \033[0;37;40m")

    for k, v in medico.items():
        print(f'{k}:\n - {v}')
    
    agenda = input('\nDigite o nome do médico que gostaria de ser atendido: ').title()
    
    if medico.get(agenda):
        print(f'\nConsulta agendada com: {medico[agenda]}')
        break
    else:
        print("\nMédico não existente, tente novamente\n")
        