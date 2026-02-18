carrinho = []

for i in range(3):
    produto = input('Qual o nome do produto? ')
    carrinho.append(produto)

print("\nCarrinho atual:", carrinho)
remover_prod = input('Qual produto você quer devolver? ')

# Código blindado contra erros!
if remover_prod in carrinho:
    carrinho.remove(remover_prod)
    print(f'Produto "{remover_prod}" removido com sucesso!')
else:
    print(f'Erro: "{remover_prod}" não estava no carrinho.')

print("Carrinho final:", carrinho)
