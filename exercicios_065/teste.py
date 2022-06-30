# def function1():
#     print("Case 1 selected")

# def function2():
#     print("Case 2 selected")

# def default():
#     print("Value default")

# if __name__ == "__main__":
#     switch = {
#         "1": function1,
#         "2": function2
#     }

#     case = switch.get("2", default)
#     case()

class Calc:

    result = 0

    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2

    def calcula(self):
        print('1 - Somar (+)\n2 - Subtrair (-)\n3 - Multiplicar (*)\n4 - Dividir (/)')
        op = int(input('Digite o número da operação desejada: '))
        if op == 1:
            self.result = self.num1 + self.num2
        if op == 2:
            self.result = self.num1 - self.num2
        if op == 3:
            self.result = self.num1 * self.num2
        if op == 4:
            self.result = self.num1 / self.num2


num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))

resultado = Calc(num1, num2)
resultado.calcula()
print(resultado.result)
