hi , mi , hf , mf = input().split()

horas = int(hf) - int(hi)
minuto = int(mf) - int(mi)

if horas <= 0:
    horas += 24
if minuto < 0:
    minuto += 60
    horas -= 1
if minuto == 0 and horas == 0:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU",horas,"HORA(S) E",minuto,"MINUTO(S)")