
class Coordinate(object):

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def set_x(self, coord_x):
        if coord_x >= 0:
            self._x = coord_x
        else:
            raise ValueError('This is not a valid coordinate')

    @property
    def y(self):
        return self._y

    @y.setter
    def set_y(self, coord_y):
        if coord_y >= 0:
            self._y = coord_y
        else:
            raise ValueError('This is not a valid coordinate')

    def distance(self, coord):
        if isinstance(coord, Coordinate):
            res_x = (self._x + coord._x) ** 2
            res_y = (self._y + coord._y) ** 2
            result = (res_x + res_y) ** 0.5
            return result
        else:
            raise ValueError('This is not a valid coordinate')

    def __str__(self):
        return f'x: {self._x} - y: {self._y}'


def main():
    coord_one = Coordinate()

    print(f'{coord_one}')
    coord_one.set_x = 5
    print(f'{coord_one}')


if __name__ == '__main__':
    main()