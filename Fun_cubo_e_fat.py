def cubo(num):
    return num ** 3

def fat(num):
    if num <= 1:
        return 1
    return num * fat(num - 1)

n = int(input('Informe um número: '))
print(n, 'ao cubo é', cubo(n))
print('O fatorial de', n, 'é', fat(n))