

l = open('cafe.txt', 'w', encoding='utf_8').write('café')
s = open('cafe.txt').read()
print(s)