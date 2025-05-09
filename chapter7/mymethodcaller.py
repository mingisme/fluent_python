from operator import methodcaller

s = 'the time has come'

upcase = methodcaller('upper')
print(upcase(s))

hyphenate = methodcaller('replace',' ','-')
print(hyphenate(s))