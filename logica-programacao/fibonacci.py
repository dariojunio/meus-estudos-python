ask_t = int(input('Quantos termos você quer mostrar? '))
t1 = int(input('Digite um número: '))
t2 = int(input('Digite o segundo número: '))

print("\n--- INICIANDO ---")
for i in range(ask_t):
    print(f'Primeiro termo: {t1} | Segundo termo: {t2}')
    t3 = t1 + t2
    print(f'Soma: {t3}\n')

    t1 = t2
    t2 = t3

print('FIM!')
