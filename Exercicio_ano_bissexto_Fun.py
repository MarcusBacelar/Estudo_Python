#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def ano_bissexto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):   #Verifica se o ano é bissexto.
        return True
    else:
        return False

def dias_mes(ano, mes):   #Retorna a quantidade de dias de um mês em um determinado ano.
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif mes == 2:
        if ano_bissexto(ano):    
            return 29
        else:
            return 28
    else:
        return 30
while True: # Começa um loop.
  ano = int(input("Digite o ano: ")) # Entrada de dados 
  mes = int(input("Digite o Mês: ")) # Entrada de dados

  if 1 <= mes <= 12:   #Verifica se atende os requisitos. 
      print(f"O ano {ano} é bissexto? {ano_bissexto(ano)}") #Saída de dados
      print(f"O mês {mes} do ano de {ano} tem {dias_mes(ano, mes)} dias.") #Saída de dados
      break #termina o loop
  else:
      print("Mês inválido.")
      #Se o mês for invalido o código volta para a entrada de dados.
      