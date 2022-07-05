# e064desafio.py
'''
Desafio:

1. Desenvolva um programa que será uma calculadora.
2. Ela tera uma "FITA" virtual.... 
3. O usuario informa qualquer tipo de função matematica (*,/,+/-,**,%,//)
4. Formatado de forma bemmm bunitinha....
5. opção de numero de casas decimais com um botão 


utilizar a funcao eval()

'''

def number_to_string(argument):
    match argument:
        case 0:
            print("zero")
        case 1:
            print("one")
        case 2:
            print("two")
        case default:
            print("something")
 
 
if __name__ == "__main__":
    argument = input("0 a 2: ")
    # argument = 0
    number_to_string(argument)

    #Não está feito