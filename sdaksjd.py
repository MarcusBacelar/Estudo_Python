aior = float('-inf')  # -∞, qualquer número pode ser maior
menor = float('inf')  # +∞, qualquer número pode ser menor
while True:
    n = float(input('Informe um número: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    resp = input('Deseja continuar? (S/N)')
    if resp.lower() == 'n':
        break
print('Maior número informado:', maior)
print('Menor número informado:', menor)
