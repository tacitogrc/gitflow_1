class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não permitida.")
        return a / b

if __name__ == "__main__":
    calc = Calculadora()
    print("Soma 1 + 2 =", calc.somar(1, 2))
