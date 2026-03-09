#usando set

l1 = set([10, 20, 30, 40])
l2 = set([15, 25, 30, 40])

print (l1 | l2) #union - unifica os sets
print (l1 - l2) #difference - valores unicos de um set
print (l1 ^ l2) #symmetric difference - valores unicos
print (l1 & l2) #and - valores duplicados
