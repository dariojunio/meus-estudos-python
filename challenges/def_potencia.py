def potencia(base, expoente=2): 
    conta = base ** expoente
    print(f'A potencia de {base} elevado a {expoente} é {conta}')


base = int(input('Digite o valor da base: '))
entrada_expoente = input('Digite o valor do expoente (ou aperte Enter para 2): ')

if entrada_expoente == "":
    #se estiver vazio, chamamos a função apenas com a base
    potencia(base)
else:
    #se o usuário digitou algo, convertemos e enviamos
    expoente = int(entrada_expoente)
    potencia(base, expoente)
