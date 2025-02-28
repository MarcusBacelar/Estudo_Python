soma = 0 #indicando q começa com zero
while True: #inicio do loop
    n = float(input('Informe um numero:'))#entrada dos números do loop
    if n ==0: #Condição para parar o loop 
        break #fechamento do loop
    soma = soma + n #Soma dos números
print('Soma dos números é:',soma) #saida.