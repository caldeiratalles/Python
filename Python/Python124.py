import sys
palavra = input()
palavra = list(palavra)
cont = 0
lista = []
contador_palavra = []
if len(palavra) == 1:
    print('1')
    sys.exit()
if len(palavra) == 2 and palavra[0] != palavra[1]:
    print('1')
    sys.exit()
if palavra == palavra[::-1]:
    print(len(palavra))
    sys.exit()
for i in range(len(palavra)):
    for j in range(len(palavra)):
        if palavra[i] == palavra[j] and not (palavra[i] in contador_palavra):
            cont+=1
        else:
            continue
    if cont % 2 ==0  and not (palavra[i] in contador_palavra):
        lista.append(cont)
        contador_palavra.append(palavra[i])
        cont = 0
        continue
    if (cont-1) % 2 == 0 and not (palavra[i] in contador_palavra):
        lista.append(cont-1)
        contador_palavra.append(palavra[i])
        cont = 0
        continue
        
    cont = 0
if sum(lista)%2==0 and sum(lista)!=0: # se for par some mais um
    print(sum(lista)+1)
    sys.exit()

if not sum(lista)%2==0:
    print(sum(lista))
    sys.exit()

            

        