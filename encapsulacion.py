
class CasillaDeVotacion:

    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property #getter son decoradores acceder por dot notation
    def region(self):
        return self._region

    @region.setter #setter
    def set_region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La región {region} no es valida en {self._pais}')


def main():
    casilla = CasillaDeVotacion(123, ['Ciudad de Mexico', 'Morelos'])
    print(casilla.region)
    casilla.set_region = 'London'
    print(casilla.region)
    casilla.set_region = 'Morelos'
    print(casilla.region)

if __name__ == '__main__':
    main()