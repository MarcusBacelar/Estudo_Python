soma = 0 # Declara valor0 a variável
lista_precos = [] # faz uma lista vazia
print('Informe o preço dos produtos') # Anúncia o pedido 
for cont in range(10): # Começa o loop de 10 produtos
    mensagem = 'Produto ' + str(cont+1) + ': ' # Mensagem de valor ao produto, adicionando 1 a mais a cada volta do loop
    preco = float(input(mensagem)) # Entrada de dados, valor do produto
    soma += preco # Calcula a soma dos valores dos produtos 
    lista_precos.append(preco) # Coloca na lista preços que anteriomente estava vazia
    media = soma / 10 # Faz o calculo da media 
print('O preço médio é', media) # Saída do valor da media
print('Os produtos com preço acima da média são:') # Anúncia a próxima etapa do código
for cont, preco in enumerate(lista_precos): # Faz um loop para achar quais produtos tem valor maior que a média
    if preco > media: # if procura preõ maior que a média
        print('Produto', cont+1) # Saída produto mais numero do loop do produto
        print('Preço: ', preco) # Saída do valor do produto 