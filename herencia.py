
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Cuadrado(Rectangulo): #Aquí se esta heredando

    def __init__(self, lado):
        super().__init__(lado, lado)


def main():
    rectangulo = Rectangulo(base = 5, altura = 3)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado = 5)
    print(cuadrado.area())


if __name__ == '__main__':
    main()