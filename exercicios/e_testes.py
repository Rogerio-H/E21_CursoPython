# e_testes.py
#------------------------------------------
# def isPalindrome(str):

# 	# Run loop from 0 to len/2
# 	for i in range(0, int(len(str)/2)):
# 		if str[i] != str[len(str)-i-1]:
# 			return False
# 	return True

# # main function
# s = input('Frase: ')
# ans = isPalindrome(s)

# if (ans):
# 	print("Yes")
# else:
# 	print("No")
#--------------------------------------------

while True:
    entrada = input("Digite entrada : ")
    if all(c.isalpha() or c.isspace() for c in entrada):
        break # sai do while
    else:
        print("Por favor digite um nome válido (somente letras e espaços)")

if str(entrada) == str(entrada)[::-1] :
    print("Palindromo")
else:
    print("nao e Palindromo")