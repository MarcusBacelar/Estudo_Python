def fat(num): #Esta linha define uma função chamada fat que recebe um argumento num. Esta função tem como objetivo calcular o fatorial do número fornecido
    
    if num <= 1: #Se num for menor ou igual a 1, a função retorna 1. Isso é importante porque o fatorial de 0 e 1 é 1.
        return 1 # Continuação da linha de cima
    
        return num * fat(num - 1) #Aqui, a função retorna o resultado de num multiplicado pelo resultado da chamada da própria função fat com o argumento num - 1
n = int(input('Informe um número: ')) #int() converte a string inserida pelo usuário em um número inteiro, que é armazenado na variável n.
print('O fatorial de', n, 'é', fat(n)) #Ela chama a função fat com o número n inserido pelo usuário e imprime a mensagem "O fatorial de n é fat(n)