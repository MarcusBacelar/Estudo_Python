#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --- Constantes ---
# Usar constantes torna o código mais legível e fácil de manter
DESCRICAO = 'DESCRIÇÃO'
ESTOQUE = 'ESTOQUE'
PRECO = 'PREÇO'


# --- Funções ---

def solicitar_inteiro(mensagem):
    """Solicita um número inteiro ao usuário com tratamento de erro."""
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")


def solicitar_float(mensagem, permite_negativo=False):
    """Solicita um número de ponto flutuante ao usuário com tratamento de erro."""
    while True:
        try:
            valor = float(input(mensagem).replace(',', '.')) # Aceita vírgula como decimal
            if not permite_negativo and valor < 0:
                print("Erro: O valor não pode ser negativo.")
            else:
                return valor
        except ValueError:
            print("Erro: Por favor, digite um número válido (ex: 10 ou 25.99).")


def cad_produto(dic_produtos):
    """Cadastra um novo produto ou atualiza um existente."""
    print('\n--- Cadastrar/Atualizar Produto ---')
    codigo = solicitar_inteiro('Código do produto: ')

    produto_novo = False
    if codigo in dic_produtos:
        produto = dic_produtos[codigo]
        print('\nProduto existente:')
        print(f"  Descrição: {produto.get(DESCRICAO, 'N/A')}")
        print(f"  Estoque atual: {produto.get(ESTOQUE, 0):.2f}")
        print(f"  Preço atual: R$ {produto.get(PRECO, 0.0):.2f}")
        print("Deixe em branco para manter o valor atual.")
    else:
        print('\nProduto não encontrado. Criando novo cadastro...')
        produto = {} # Cria um dicionário vazio para o novo produto
        dic_produtos[codigo] = produto
        produto_novo = True

        # Solicita descrição apenas para produtos novos
        while True:
            descricao = input('Informe a descrição: ').strip()
            if descricao:
                produto[DESCRICAO] = descricao
                break
            else:
                print("Erro: A descrição não pode ser vazia.")

    # Solicita Estoque (permite atualizar ou definir inicial)
    while True:
        prompt_estoque = f"Novo Estoque{' (Atual: ' + str(produto.get(ESTOQUE, 'N/A')) + ')' if ESTOQUE in produto else ''}: "
        try:
            estoque_str = input(prompt_estoque).strip().replace(',', '.')
            if not estoque_str and ESTOQUE in produto: # Mantem o atual se deixar em branco e já existir
                print(f"Mantendo estoque atual: {produto[ESTOQUE]:.2f}")
                break
            elif not estoque_str and ESTOQUE not in produto:
                 print("Erro: Estoque inicial precisa ser definido.")
                 continue # Pede novamente

            novo_estoque = float(estoque_str)
            if novo_estoque < 0:
                print("Erro: Estoque não pode ser negativo.")
            else:
                produto[ESTOQUE] = novo_estoque
                break
        except ValueError:
            print("Erro: Valor de estoque inválido. Use números (ex: 10 ou 10.5).")


    # Solicita Preço (permite atualizar ou definir inicial)
    while True:
        prompt_preco = f"Novo Preço{' (Atual: R$ ' + str(produto.get(PRECO, 'N/A')) + ')' if PRECO in produto else ''}: "
        try:
            preco_str = input(prompt_preco).strip().replace(',', '.')
            if not preco_str and PRECO in produto: # Mantem o atual se deixar em branco e já existir
                print(f"Mantendo preço atual: R$ {produto[PRECO]:.2f}")
                break
            elif not preco_str and PRECO not in produto:
                 print("Erro: Preço inicial precisa ser definido.")
                 continue # Pede novamente

            novo_preco = float(preco_str)
            if novo_preco < 0:
                 print("Erro: Preço não pode ser negativo.")
            else:
                 produto[PRECO] = novo_preco
                 break
        except ValueError:
            print("Erro: Valor de preço inválido. Use números (ex: 25.99).")


    print("\nProduto cadastrado/atualizado com sucesso!")
    print(f"CÓDIGO: {codigo} | {produto}")
    input('Pressione ENTER para continuar...')


def listar_produtos(dic_produtos):
    """Lista todos os produtos cadastrados."""
    print('\n--- Lista de Produtos ---')
    if not dic_produtos: # Maneira mais pythonica de verificar se está vazio
        print('Nenhum produto cadastrado!')
    else:
        # Imprime um cabeçalho
        print(f"{'CÓDIGO':<8} | {'DESCRIÇÃO':<25} | {'ESTOQUE':>10} | {'PREÇO (R$)':>12}")
        print("-" * 60) # Linha separadora

        # Itera e imprime cada produto formatado
        for codigo, produto in dic_produtos.items():
            desc = produto.get(DESCRICAO, 'N/A') # Usa N/A se não houver descrição
            est = produto.get(ESTOQUE, 0.0)      # Usa 0.0 se não houver estoque
            prc = produto.get(PRECO, 0.0)        # Usa 0.0 se não houver preço
            print(f"{codigo:<8} | {desc:<25} | {est:>10.2f} | {prc:>12.2f}")

        print("-" * 60) # Linha separadora no final

    # Pausa no final, fora do loop
    input('Pressione ENTER para voltar ao menu...')


def venda(dic_produtos, lista_vendas):
    """Registra a venda de um produto, atualizando o estoque."""
    print('\n--- Venda de Produto ---')
    if not dic_produtos:
        print("Nenhum produto cadastrado para vender.")
        input('Pressione ENTER para continuar...')
        return

    codigo = solicitar_inteiro('Código do produto vendido: ')

    if codigo not in dic_produtos:
        print('Erro: Produto não encontrado!')
        input('Pressione ENTER para continuar...')
        return

    produto = dic_produtos[codigo]
    print('\nProduto selecionado:')
    print(f"  Descrição: {produto.get(DESCRICAO, 'N/A')}")
    print(f"  Estoque disponível: {produto.get(ESTOQUE, 0):.2f}")
    print(f"  Preço unitário: R$ {produto.get(PRECO, 0.0):.2f}")

    estoque_atual = produto.get(ESTOQUE, 0) # Pega estoque ou 0 se não existir
    preco_unitario = produto.get(PRECO, 0.0) # Pega preço ou 0 se não existir

    if estoque_atual <= 0:
        print("\nErro: Produto sem estoque disponível para venda.")
        input('Pressione ENTER para continuar...')
        return

    while True:
        quant = solicitar_float('Quantidade vendida: ')
        if quant <= 0:
            print("Erro: A quantidade vendida deve ser maior que zero.")
        elif quant > estoque_atual:
            print(f'\nErro: Estoque insuficiente! Disponível: {estoque_atual:.2f}')
            # Não retorna, permite tentar novamente com quantidade menor
        else:
            break # Quantidade válida

    # Calcula total, registra venda e atualiza estoque
    total_venda = preco_unitario * quant
    print(f'\nTotal da venda: R$ {total_venda:.2f}')

    # Cria a tupla da venda (código, quantidade, preço NO MOMENTO da venda)
    venda_registrada = (codigo, quant, preco_unitario)
    lista_vendas.append(venda_registrada)

    # Atualiza o estoque no dicionário de produtos
    produto[ESTOQUE] = estoque_atual - quant

    print("Venda registrada e estoque atualizado com sucesso!")
    input('Pressione ENTER para continuar...')


def relatorio_vendas(dic_produtos, lista_vendas):
    """Exibe um relatório com todas as vendas realizadas."""
    print('\n--- Relatório de Vendas ---')
    if not lista_vendas:
        print('Nenhuma venda registrada!')
    else:
        total_geral = 0
        # Imprime cabeçalho
        print(f"{'CÓDIGO':<8} | {'PRODUTO':<25} | {'QUANT.':>8} | {'PREÇO UN.(R$)':>15} | {'TOTAL (R$)':>12}")
        print("-" * 75)

        # Itera sobre a lista de tuplas de vendas
        for codigo, quant, preco_venda in lista_vendas:
            # Busca a descrição atual do produto (pode ter sido alterada)
            produto_atual = dic_produtos.get(codigo, {DESCRICAO: 'Produto Excluído'}) # Trata caso produto seja deletado
            descricao_prod = produto_atual.get(DESCRICAO, 'Descrição Indisponível')

            total_item = quant * preco_venda
            print(f"{codigo:<8} | {descricao_prod:<25} | {quant:>8.2f} | {preco_venda:>15.2f} | {total_item:>12.2f}")
            total_geral += total_item

        print("-" * 75)
        print(f"{'TOTAL GERAL DAS VENDAS:':<60} R$ {total_geral:>12.2f}") # Alinha o total geral
        print("-" * 75)

    # Pausa no final
    input('Pressione ENTER para voltar ao menu...')


def menu():
    """Exibe o menu principal e retorna a opção do usuário."""
    print('\n*********************************')
    print('* MENU PRINCIPAL        *')
    print('*********************************')
    print('* (C)adastrar/Atualizar Produto *')
    print('* (L)istar Produtos             *')
    print('* (V)ender Produto              *')
    print('* (R)elatório de Vendas         *')
    print('* (S)air                        *')
    print('*********************************')
    escolha = input('Informe sua opção: ').upper().strip() # Converte para maiúsculo e remove espaços
    return escolha


def principal():
    """Função principal que executa o programa."""
    lista_vendas = []
    dic_produtos = {} # Dicionário para armazenar os produtos

    # Dados de exemplo (opcional, pode remover ou comentar)
    # dic_produtos = {
    #     101: {DESCRICAO: 'Caneta Azul', ESTOQUE: 50.0, PRECO: 1.50},
    #     102: {DESCRICAO: 'Lápis HB', ESTOQUE: 100.0, PRECO: 0.80},
    #     205: {DESCRICAO: 'Caderno 10 Matérias', ESTOQUE: 20.0, PRECO: 15.99}
    # }

    while True:
        escolha = menu()

        if escolha == 'C':
            cad_produto(dic_produtos)
        elif escolha == 'L':
            listar_produtos(dic_produtos)
        elif escolha == 'V':
            venda(dic_produtos, lista_vendas)
        elif escolha == 'R':
            relatorio_vendas(dic_produtos, lista_vendas)
        elif escolha == 'S':
            print("\nSaindo do programa. Até logo!")
            break # Encerra o loop while
        else:
            print("\nOpção inválida! Por favor, escolha uma das opções do menu.")
            input('Pressione ENTER para tentar novamente...')


# --- Execução Principal ---
if __name__ == '__main__':
    principal()