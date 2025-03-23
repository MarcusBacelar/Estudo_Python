#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("Calculadora de MMC e MDC") # Anúncio sobre o projeto
def calcular_mdc(a,b): # Função para calcular o MDC 
    while(b): #Loop continua enquanto b for diferente de zero
        a , b = b, a % b
    return a # Quando b se torna zero, o loop termina, e o valor de a (que é o MDC) é retornado

def calcular_mmc(a,b): # Função para calcular o MMC
    return abs (a * b) // calcular_mdc(a,b) # Chama a função calcular_mdc para obter o MDC de a e b //: Realiza a divisão inteira (descarta a parte decimal)

def main(): # Flunção da lógica principal do programa
    while True: # Começo do loop
        try: # Para o código continuar rodando mesmo com erro
            num1 = int(input("Escreva o primeiro numero: ")) # Entrada de dados
            num2 = int(input("Escreva o segundo numero: ")) # Entrada de dados

            mdc = calcular_mdc(num1, num2) # Chama a função
            mmc = calcular_mmc(num1, num2) # Chama a função

            print(f"O MDC de {num1} e {num2} é {mdc}")  # Saída de dados
            print(f"O MMC de {num1} e {num2} é {mmc}")  # Saída de dados
            break # Fecha o loop 
        except ValueError: #Indentifica o erro
            print("Entrada inválida, por favor digite numeros inteiros.") # Mensagem de erro

if __name__ == "__main__": #é uma convenção Python que permite que você controle o comportamento do seu script dependendo de como ele é executado.
    main()