print("Calcule o fatorial!!!")
      
n = int(input('Informe um número: '))
fat = 1
for cont in range(n, 1, -1): #começo e final do loop 
    fat *= cont
print('O fatorial de', n, 'é', fat)