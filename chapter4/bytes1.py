import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)

print(octets)


for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')

city = 'São Paulo'

city1=city.encode('cp437', errors='ignore')
print(city1)

octets = b'Montr\xe9al'
octets1 = octets.decode('utf_8', errors='replace')
print(octets)