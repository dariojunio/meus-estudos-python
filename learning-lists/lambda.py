#lambda - usada dentro de funcoes como uma sub funcao

q = lambda x,y: x - y + 10
print(q(10, 10))

#--------------------------------------

def somar(z):
  func2 = lambda z: z - 5
  return func2(z) + 10

print(somar(-5))
