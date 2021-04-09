contador = 0
lista = []
while contador<2:
    nota = float(input())
    if 0<=nota<=10:
        lista.append(nota)
        contador+=1
        continue
    if nota<0 or nota>10:
        print('nota invalida')
        continue
media = sum(lista)/len(lista)
print('media =', media)
