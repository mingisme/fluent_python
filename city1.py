from collections import namedtuple
import json

City = namedtuple('City', 'name country population coordinates')

print(City._fields) #('name', 'country', 'population', 'location')

Coordinate = namedtuple('Coordinate', 'lat lon')

delhi_data = ('Delhi NCR', 'IN', 21.935, Coordinate(28.613,77.208))

delhi = City._make(delhi_data)

print(delhi._asdict())

print(json.dumps(delhi._asdict()))
