soma = 0 # inicia a variável com valor 0.
lista_precos = [] # Cria uma lista vazia.

print('Informe o preço dos produtos') # Pedido ao Usuário.

for cont in range(10): # Inicia um loop que se repete 10 vezes. A variável cont assume valores de 0 a 9.
    mensagem = 'Produto ' + str(cont+1) + ': ' #  Cria uma mensagem para pedir o preço de cada produto. Por exemplo, na primeira iteração,
                                               #   mensagem será  "Produto 1: "/ "(cont + 1)" mostra em qual parte do loope está.
    preco = float(input(mensagem)) # Entrada do valor do produto / Float pois pode ser numero quebrado. 
    soma += preco # Adiciona o preço digitado para a variável soma.
    lista_precos.append(preco) # Adiciona o preço digitado à lista lista_precos.
    media = soma / 10 # Calcula a média
 
print('O preço médio é', media) # Exibe a média calculada.
print('Os preços acima da média são:') # Exibe uma mensagem informando que os preços acima da média serão mostrados.

for preco in lista_precos: # inicia um loop que percorre todos os preços armazenados na lista lista_precos.
    if preco > media: # Se o preço for maior que a media, ele mostra o preço conquitantemente.
        print(preco) # Exibe os preços maiores que a media.
