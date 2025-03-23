#!/usr/bin/env python3
# -*- coding: utf-8 -*-
Mensagem = "Digite um número inteiro: " #Declaração da váriavel Mensagem


def Input_Mensagem(): #Começo da função 
    while True:
        try:
            return int(input(Mensagem))
        except ValueError:  # Especifica o tipo de erro
            print("Número inválido! Tente novamente.")


numero = Input_Mensagem()
print("O número digitado foi:", numero)
