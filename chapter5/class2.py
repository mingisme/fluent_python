import typing

Coordinate = typing.NamedTuple('Coordinate', [('lat', float), ('lon', float)])

b1 = issubclass(Coordinate, tuple)
print(b1)

print(typing.get_type_hints(Coordinate))

