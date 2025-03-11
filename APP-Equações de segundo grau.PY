import math

print('Informe os termos da equação Ax² + Bx + C')
a = int(input('Digite o valor de A:'))
b = int(input('Digite o valor de B:'))
c = int(input('Digite o valor de C:'))


if a == 0:
    print(' *A* não pode ser igual a zero(0).')

else:
    delta = b**2 - 4*a*c

    if delta < 0:
        print('A equação não tem raizes.')

    elif (delta == 0):
        x1 = -b / (2 * a)
        print('A equação possui a raiz', x1)

    else:
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)
        print('A equação possui duas raizes:')
        print('X1= ', x1)
        print('X2= ', x2)
