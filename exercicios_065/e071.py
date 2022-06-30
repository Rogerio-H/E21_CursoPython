# e071.py

# 71. Crie uma calculadora simples de 4 operações (soma,sub,multi e div)
#  usando apenas de estrutura de código orientada a objetos.
# Ex. calc.soma(3,4); calc.div(9,3) (11)

class Calculadora:
    def soma(self, p1, p2):
        return (p1 + p2)
    
    def sub(self, p1, p2):
        return(p1 - p2)

    def div(self, p1, p2):
        return (p1 / p2)

    def multi(self, p1, p2):
        return(p1 * p2)

calc = Calculadora()
print(calc.soma(3, 4))
print(calc.sub(4, 3))
print(calc.div(9, 3))
print(calc.multi(2, 4))