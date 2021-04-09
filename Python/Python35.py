n = int(input()) #5400 = n
#segundos em horas direto
h = n // 60**2
#passou para segundos para subtrair de n
n = n - h * 60**2 #1800 = n
#pegou o resto da subtração e transformou em minutos
m = n // 60
#pegou o resto da subtração de minutos transformados em segundos
n = n - m*60 # n = 0

s = n

print('{}:{}:{}'.format(h, m, s))