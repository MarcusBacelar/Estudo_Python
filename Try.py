import math
while True:
    try:
        print("Informe um numero!!!")
        N = float(input("Digite seu numero: "))
        Num = (N*2)/2
        print("Seu numero * 2 / 2 = ", Num)
        break
    except:
        print('Ocorreu o seguinte erro:', type(N))
