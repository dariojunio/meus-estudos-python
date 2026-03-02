def atualizar_estoque(quantidade_venda, estoque_atual):
  
  if quantidade_venda < estoque_atual:
    estoque_atual -=quantidade_venda
    print (f'Voce vendeu {quantidade_venda} tenis, boa!')
    print (f'Estoque atualizado, agora temos {estoque_atual} disponiveis na loja')
    return estoque_atual
  else:
    print ('Estoque insuficiente!')
    return estoque_atual



while True:
  print ('===== LOJINHA DO D9 =====')
  print (f'Temos {estoque_tenis} tenis disponiveis!')
  print ('----- Painel de controle -----')
  painel = int(input('Pressione [1] para cadastrar uma venda, aperte [0] para sair '))

  if painel == 1:
      vendas_tenis = int(input('Quantos tenis foram vendidos nessa venda?'))
      estoque_tenis = atualizar_estoque(vendas_tenis, estoque_tenis)
  else:
    print('Fechando painel de controle da loja.')
    break
  
