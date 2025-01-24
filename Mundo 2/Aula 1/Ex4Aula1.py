nota1 = float(input('Digite a nota do aluno: '))
nota2 = float(input('Digite a nota do aluno: '))

media = (nota1 + nota2) / 2

if media < 5:
    print(f'A media do aluno foi {media} portanto o mesmo está reprovado')

elif media >= 5 and media <= 6.9:
    print(f'A media do aluno foi {media} portanto o mesmo está em recuperação')

else:
    media >= 7
    print(f'A media do aluno é {media} portanto o mesmo está aprovado')