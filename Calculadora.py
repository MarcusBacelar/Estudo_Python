A=0
resul = 0
while True:
    resp=input("Calculadora digite +, -, / ou * para fazer a equação (ou s para sair) :")

    
    if resp == "s":
       
        break
    else:
        n1 = input('Digite o valor do primeiro numero:')
        n2= input('Digite o valor do segundo numero:')
        if resp == '+':
            resul = (n1 + n2)
            print('Resultado é: ', resul)
