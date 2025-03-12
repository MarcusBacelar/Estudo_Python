while True:
    try:
        print('Informe dois números')
        n1 = float(input('n1: '))
        n2 = float(input('n2: '))
        r = n1 / n2
        break
    except Exception as e:
        print('Ocorreu o seguinte erro:', type(e))
print(n1, '/', n2, '=', r)