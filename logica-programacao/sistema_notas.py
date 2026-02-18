def notas_alunos(nota_aluno, nome_aluno):
    if nota_aluno < 4:
        print(f'{nome_aluno}, você tirou {nota_aluno:.2f} e não passou!')
    elif nota_aluno < 7:
        print(f'{nome_aluno}, você tirou {nota_aluno:.2f} e ficou de recuperação!')
    else:
        print(f'{nome_aluno}, você tirou {nota_aluno:.2f} e passou!! Parabéns!')

nome_aluno = input('Qual o nome do aluno? ')
nota_aluno = float(input('Qual a nota do aluno? '))

notas_alunos(nota_aluno, nome_aluno)
