num_maior,n_menor = input('').split()
num_maior = int(num_maior)
n_menor = int(n_menor)
contador = n_menor
lista = []

while contador<=num_maior:
	lista.append(contador)
	contador +=1
for i in lista:
	print(str(i)+ ' ',end='')
soma = sum(lista)
print('Sum='+str(soma))


#contrl+alt+enter



