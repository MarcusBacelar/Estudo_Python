while True: #começo do loop
    try: #Continuar a executar o código mesmo com erro
        print('Informe dois números')
        n1 = float(input('n1: '))
        n2 = float(input('n2: '))
        r = n1 / n2
        break
    except ValueError as e: #Mostrar o erro numero inválido
        print(e)
        print('Número inválidos! Tente novamente.')
    except ZeroDivisionError as e: #Mostrar o erro divisão por zero
        print(e)
        print('Divisão por zero! Tente novamente.')
print(n1, '/', n2, '=', r)