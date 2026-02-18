notas = []

for i in range(3):
    nota = float(input(f'Digite a nota {i+1} do aluno: '))
    notas.append(nota)

nf = sum(notas) / len(notas)

if nf < 5:
    print(f'O aluno teve no mês a média de: {nf:.2f} e reprovou na matéria.')
elif nf < 7:
    print(f'O aluno teve no mês a média de: {nf:.2f} e ficou de recuperação.')
else:
    print(f'O aluno teve no mês a média de: {nf:.2f} e passou na matéria!!')
