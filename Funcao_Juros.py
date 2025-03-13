def juros(capital,taxa,juros=12): #Esta linha define uma função chamada juros que calcula o valor dos juros simples.
    return(capital*taxa*juros)/100 #A fórmula para calcular juros simples é: (capital * taxa * tempo) / 100. A função implementa essa fórmula e retorna o resultado.


temp=0 #Iqualado a zero para ter valor inicial

print("Cálculo de juros simples") #Saida de mesagem 

cap=float(input("Digite o valor do capital: ")) #Esta linha solicita ao usuário que digite o valor
tax=float(input("Digite o valor da taxa: ")) #Esta linha solicita ao usuário que digite o valor
temp=input('tempo(deixe em branco para o padrão de 12): ') #Esta linha solicita ao usuário que digite o valor

if temp == '': # Este bloco if-else verifica se o usuário digitou um valor para o tempo
    jur=juros(cap,tax)

else:   #Caso contrário, a entrada do usuário é convertida em um número decimal usando float()
    temp=float(temp)
    jur=juros(taxa=tax,capital=cap,tempo=temp)

print("O valor dos juros é ", jur) #Saída mensagem resultado 