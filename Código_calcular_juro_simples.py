print('Informe os dados para o cálculo dos juros')
c = float(input('Capital: '))
tx = float(input('Taxa de juros: '))
t = float(input('Tempo: '))
j = c* tx * t / 100
print('O valor dos juros é', j)
