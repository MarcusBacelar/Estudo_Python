print("Digite os três numeros:")
n1=int(input('Digite o primeiro numero:'))
n2=int(input('Digite o segundo numero:'))
n3=int(input('Digite o terceiro numero:'))

if n1>n2>n3:
    print('O maior numero é: ', n1)
elif n2>n3>n1:
    print('O maior numero é: ', n2)
elif n3>n2>n1:
    print('O maior numero é: ', n3)
else:
    print('Os numeros são iguais.')