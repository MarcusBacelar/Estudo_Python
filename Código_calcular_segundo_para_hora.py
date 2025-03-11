Total_segundo = int(input('Digite um numero em segundos, para transformar ele em hora, minuto e segundo:'))
Minutos = Total_segundo // 60
segundos = Total_segundo % 60
horas = Minutos // 60
Minutos %= 60
print(horas, ':', Minutos, ':', segundos)