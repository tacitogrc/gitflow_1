from calculadora import Calculadora

class CalculadoraCientifica(Calculadora):
    def potencia(self, base, expoente):
        return base ** expoente

    def raiz_quadrada(self, valor):
        if valor < 0:
            raise ValueError("Raiz quadrada de número negativo não é permitida.")
        return valor ** 0.5
