ano=int(input('DIgite o ano:'))

if (ano % 400 ==0) or (ano %4 ==0 and ano %100 !=0):
    print('Ano Bissexto.')
else:
    print('Ano não Bissexto')