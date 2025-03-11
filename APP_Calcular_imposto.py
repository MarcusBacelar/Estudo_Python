print('Calcular o imposto de renda:')
salario = float(input('Digite o valor do seu salario:'))

if salario <= 1909.98:
    imposto = 0
elif salario <= 2826.65:
    imposto = salario * 7.5/100
elif salario <= 3751.05:
    imposto = salario * 15/100
elif salario <=4664.68:
    imposto= salario *22,5/100
else:
    imposto = salario *27.5/100
print('o imposto de renda é: ',imposto )