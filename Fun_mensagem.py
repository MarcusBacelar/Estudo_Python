#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def input_int(mensagem):  # Declarar função mensagem
    while True:  # Abrir loop
        try:  # Rodar mesmo com erro e especificar o erro
            # Usa a mensagem passada como argumento
            numero = int(input(mensagem))
            return numero
        except ValueError:  # Especifica o erro ValueError
            print("Número inválido, digite um número inteiro.")


idade = input_int("Digite sua idade: ")  # Entrada de dados
print(f"Sua idade é {idade}")   # Saída de dados

numero_favorito = input_int("Digite seu número favorito: ")  # Entrada de dados
print(f"Seu numero favorito é {numero_favorito}")  # Saída de dados
