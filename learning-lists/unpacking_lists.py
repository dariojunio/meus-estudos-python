#unpacking lists

p = ['arroz', 'feijao', 'carne']

i1, i2, i3 = p

print(i1)
print(i2)
print(i3)

#--------------------------------------------

n = [10, 20, 15, 17, 19,  30]

n1, n2, *outros, n5 = n #consigo ignorar valores na associacao com *

print(n1)
print(n2)
print(outros)
print(n5)
