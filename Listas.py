# Lista inicializada com números de 0 a 9
lista = list(range(10))
print(lista)

# Lista de 10 posições com valores 0
lista = [0]*10
print(lista)


# Lista inicializada com números de 0 a 9
lista = [n for n in range(9)]
print(lista)


# Leitura de string e com split
texto = input('Informe números (separados com espaços): ')
lista = [int(x) for x in texto.split()]
print(lista)
print(len(lista))