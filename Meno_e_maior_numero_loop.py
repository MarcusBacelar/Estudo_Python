maior = float('-inf')  # Inicializa o maior número com infinito negativo
menor = float('inf')  # Inicializa o menor número com infinito positivo

print("Digite números. Para parar, digite 'n' quando solicitado.")

while True:
    try:
        n = input('Digite um número ou "n" para sair: ')
        if n.lower() == 'n':
            break
        n = float(n)  # Converte a entrada para um número

        if n > maior:
            maior = n
        if n < menor:
            menor = n

    except ValueError:
        print("Entrada inválida. Digite um número válido ou 'n' para sair.")

print("O maior número é:", maior)
print("O menor número é:", menor)