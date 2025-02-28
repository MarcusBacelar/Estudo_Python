print('Olá Aluno.')
nota = float(input('Informe a nota:'))

if nota == 100:  # Condição para nota máxima verificada primeiro
    print('Parabéns pela nota máxima!!!')
elif nota >= 60:
    print('Aprovado')  # Removida a atribuição desnecessária A =
    print('Boas Férias')
elif nota >= 40:
    print('Recuperação')
else:
    print('Reprovado')