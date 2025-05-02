from collections import namedtuple

Coordinate = namedtuple('Coordinate', 'lat lon')

b1 = issubclass(Coordinate, tuple)
print(b1)

moscow = Coordinate(55.756, 37.617)
print(moscow)
print(moscow == Coordinate(55.756, 37.617))