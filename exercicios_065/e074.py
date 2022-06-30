# e074.py

class Calc():
    
    result = 0
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calcula(self):
        print('1 - Somar (+)\n2 - Subtrair (-)\n3 - Multiplicar (*)\n4 - Dividir (/)')
        result = int(input('Digite o número da operação: '))

        match result:
            case 1:
                self.result = (self.num1 + self.num2)
            case 2:
                self.result = (self.num1 - self.num2)
            case 3:
                self.result = (self.num1 * self.num2)
            case 4:
                self.result = (self.num1 / self.num2)
            

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

resultado = Calc(num1, num2)
resultado.calcula()
print(resultado.result)