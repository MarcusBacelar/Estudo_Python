def calcula(expr):
    """
    Função que calcula o resultado de uma expressão matemática.

    Args:
        expr (str): A expressão matemática a ser calculada.

    Returns:
        int or float or None: O resultado da expressão, ou None se a expressão for inválida.
    """
    try:
        return eval(expr)  # Tenta avaliar a expressão usando a função eval()
    except:
        print('Expressão inválida!')  # Imprime uma mensagem de erro se a expressão for inválida
        return None  # Retorna None para indicar que a expressão não pôde ser calculada

HIST = ''  # Inicialização da variável global HIST, que armazena o histórico de cálculos

def historico(expr, res):
    """
    Função que armazena a expressão e o resultado no histórico.

    Args:
        expr (str): A expressão matemática calculada.
        res (int or float or None): O resultado da expressão.
    """
    global HIST  # Indica que a variável HIST é global
    if res is not None:  # Verifica se o resultado é válido (não é None)
        HIST += '\n\n' + expr  # Adiciona a expressão ao histórico
        HIST += '\n' + str(res)  # Adiciona o resultado ao histórico

def principal():
    """
    Função principal que interage com o usuário, recebe expressões, calcula e exibe resultados.
    """
    while True:  # Loop infinito para receber expressões continuamente
        print('Informe a expressão matemática')
        print('(<h> para histórico, <s> para sair)')
        expr = input()  # Recebe a expressão do usuário
        if expr.lower() == 'h':  # Verifica se o usuário quer ver o histórico
            print(HIST, '\n')  # Imprime o histórico
        elif expr.lower() == 's':  # Verifica se o usuário quer sair
            break  # Sai do loop
        else:
            res = calcula(expr)  # Calcula o resultado da expressão
            historico(expr, res)  # Adiciona a expressão e o resultado ao histórico
            print(res, '\n')  # Imprime o resultado

if __name__ == '__main__':
    principal()  # Chama a função principal se o script for executado diretamente