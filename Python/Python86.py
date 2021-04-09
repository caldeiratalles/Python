import sys
number_caract = int(input())
string = input()
timina = 0
adenosina = 0
citosina = 0
guanina = 0
t = 0
interroga = 0
contador=1
while contador <= number_caract:
    if number_caract%2==1:
        contador=contador+1
        print("Feiticeiro misterioso")
        sys.exit()
    else:
        break
while t < number_caract:
    c = string[t]
    if c=='A':
        adenosina+=1
        
    if c=='C':
        citosina+=1
        
    if c=='G':
        guanina+=1
        
    if c=='T':
        timina+=1
        
    if c=='?':
        interroga +=1
        
    t += 1
soma = adenosina+citosina+guanina+timina+interroga
if soma%4!=0:
    print('Feiticeiro misterioso')
    sys.exit()
if adenosina>(soma/4) or citosina>(soma/4) or guanina>(soma/4) or timina>(soma/4):
    print('Feiticeiro misterioso')
else:
    print('Segredos desvendados')
