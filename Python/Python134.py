valor = int(input())
a = input().split()
lista = []
contador = 1
listaTira = []
contador1 = 0
for i in range(len(a)): #varrendo string e transformando em int
    a[i]= int(a[i])
while contador<valor+1:
    lista.append([contador,a[contador1]])
    contador+=1
    contador1+=1
print(lista)
 
