
cafe = bytes('café', encoding='utf_8')
print(cafe)

print(cafe[0])

print(cafe[:1])

cafe_arr = bytearray(cafe)
print(cafe_arr)

print(cafe_arr[-1:])

bytes1 = bytes.fromhex('31 4B CE A9')
print(bytes1)