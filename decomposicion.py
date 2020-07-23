
class Automovil:
    
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.modelo = marca
        self.color = color
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4)
        self._seguridad = airbag()

    def acelerar(self, tipo):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
            self._motor.temperatura(12)
        else:
            self._motor.inyecta_gasolina(3)
            self._motor.temperatura(7)

        self._estado = 'en movimiento'

    def desacelerar(self, tipo='choque'):
        if tipo == 'choque':
            self._seguridad.activar()


class Motor:
    
    def __init__(self, cilindros, tipo='gasolina', nivelgasolina=10000):
        self.cilindros = cilindros
        self.tipo = tipo
        self.temperatura_c = 0
        self.nivelgasolina = nivelgasolina

    def inyecta_gasolina(self, cantidad):
        self.nivelgasolina = self.nivelgasolina - cantidad

    def temperatura(self, grados):
        self.temperatura_c = self.temperatura_c + grados

    def information(self):
        print('\n')
        print(f'Nivel de gasolina = {self.nivelgasolina} \n')
        print(f'Temperatura = {self.temperatura_c}')


class airbag:

    def __init__(self, estado='optimo'):
        self.estado = estado

    def activar(self):
        print('AIRBAG ACTIVADO')
        self.estado = 'inhabilitado'


def main():
    car1 = Automovil('2020', 'TOYOTA', 'AZUL')
    car1._motor.information()
    car1.acelerar('rapida')
    car1._motor.information()
    car1.desacelerar('choque')

if __name__ == '__main__':
    main()