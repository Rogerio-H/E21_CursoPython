# e098.py

# nota_americano = {"A": "1.0", "B": "0.9", "C": "0.8", "D" : "0.7", "E" : "0.6",
# "F" : "0.5", "G": "0.4", "H" : "0.3", "I" : "0.2", "J" : "0.1", "K" : "0.0"}

while True:
    nota = input("Digite sua nota ('A - F'): ").upper()  

    match nota:
        case "A":
            print("Gabaritou")
            break
        case "B" | "C":
            print("Aprovado!")
            break
        case "D" | "E":
            print("Reprovado!")
            break
        case "F":
            print("Zerou!")
            break
        case default:
            print("É com letras de A à F!!!")





# def calcula_nota(nota_americano):
#     nota_americano = {"1.0" == "A", "B" == "0.9", "C" == "0.8", "D" == "0.7", "E" == "0.6",
#         "F" == "0.5", "G"== "0.4", "H" == "0.3", "I" == "0.2", "J" == "0.1", "K" == "0.0"}
#     match nota_americano:
#         case "A":
#             print("Gabaritou!")
#         case "B", "C", "D", "E":
#             print("Aprovado!")
#         case "F", "G", "H", "I", "J", "K":
#             return ("Reprovado!")
#         # case default:
#         #     return "Digite pelo modelo americano (o modelo americano é 'A, B, C') "


# nota_americano = str((input("Digite sua nota: "))).upper()
# # float(nota)
# print(calcula_nota(nota_americano))
# print(type(calcula_nota(nota_americano)))

    
    
    
    
#     if nota < 0 or nota > 1.0:
#         print('Pontuacao invalida')
#         print('A nota deve ser um valor entre 0 e 1.0')
#     elif nota == 1.0:
#         print('Parabens, você gabaritou a prova!!!')
#     elif nota >= 0.6:
#         print("Parabens voce foi aprovado(a)")
#     elif nota < 0.6:
#         print('Nota abaixo da média vc está em recuperação')
#     else: 
#         print("Não foi posssivel computar sua nota!!!")



# try:
#     nota = float(input('Digite uma nota:'))
# except:
#     print("Valor Invalido")
#     print("Use somente os numeros com casas decimais dentre 0 e 1.0")

# print(calcula_nota(nota))