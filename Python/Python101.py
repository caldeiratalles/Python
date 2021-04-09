contador_1 = 0 #Álcool
contador_2 = 0 #Gasolina
contador_3 = 0 #Diesel

while True:
	codigo = int(input())
	if codigo==1:
		contador_1+=1
	if codigo==2:
		contador_2+=1
	if codigo==3:
		contador_3+=1
	if codigo==4:
		break
	if codigo!=1 and codigo!=2 and codigo!=3 and codigo!=4:
		continue
print('MUITO OBRIGADO')
print('Alcool:',contador_1)
print('Gasolina:',contador_2)
print('Diesel:',contador_3)
