def fatorial(numero):
    resultado = 1
    #se o número for 0 ou 1, o fatorial é 1
    if numero < 0:
        return "Não existe fatorial de número negativo"
    #fazemos um loop de 1 até o próprio número
    for n in range(1, numero + 1):
        resultado *= n
        
    print(f'{numero}! é igual a {resultado}')

x = int(input('Digite um numero para fatorar '))
fatorial(x)
