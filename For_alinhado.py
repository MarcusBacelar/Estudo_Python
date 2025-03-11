n = int(input('Informe o número de elementos do conjunto: '))
print('Elementos:', end=' ')
for cont in range(1, n+1):
    print(cont, end=' ')
print('\nCombinações:', end='')
for cont in range(1, n+1):
    for cont2 in range(1, n+1):
        print('(', cont, ', ', cont2, ')', sep='', end=' ')
