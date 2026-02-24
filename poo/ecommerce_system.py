class Produto:
  def __init__(self, produto, valor):
    self.produto = produto
    self.valor = valor



class Cliente:
  def __init__(self, nome):
    self.nome = nome
    self.carrinho = []

  def adicionar_produto(self, item):
    self.carrinho.append(item)

  def listar_carrinho(self):
    print(f'\n==== Carrinho de {self.nome} ====')
    for i in self.carrinho:
      print(f'O produto {i.produto} custa R${i.valor:.2f}.')

  def somar_produtos(self):
    total = 0
    for i in self.carrinho:
      total = total + i.valor

    print(f'Sua compra deu um total de R${total:.2f}')
    

p1 = Produto(produto='i5-14600f',valor=2400.50)
p2 = Produto(produto='RTX 5060 TI', valor=2000.99)
p3 = Produto(produto='Monitor Samsumg 23p 144h', valor=899.99)
p4 = Produto(produto='Teclado Redragon Draconic', valor=389.99)


cliente1 = Cliente('Zed')
cliente1.adicionar_produto(p1)
cliente1.adicionar_produto(p2)
cliente1.adicionar_produto(p3)
cliente1.adicionar_produto(p4)

cliente1.listar_carrinho()
cliente1.somar_produtos()



