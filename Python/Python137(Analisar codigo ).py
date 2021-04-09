inputs = int(input())
ai = input().split()
dicionario = {} #dicionario de valor
dicionario2 = {} #dicionario de chaves
#dicionario de chaves
for i in range(inputs):
    dicionario2[i] = i
#varrendo string e transformando em int
for i in range(inputs): 
    ai[i]= int(ai[i])
#dicionario criando o de valores
for i in range(len(ai)):
    dicionario[i] = ai[i]
#condições
contador = 0
for i in range(len(dicionario)):
    for j in range(len(dicionario)):
        # i < j ?
        if dicionario2[i]<dicionario2[j] and not :
            if dicionario[i]==dicionario[j]:
                contador+=1
        else:
            continue
print(contador)

#n = int(input())
#a = [int(x) for x in input().split()]

#cnt = {}

#for x in a:
#    if x not in cnt:
#        cnt[x] = 0

#    cnt[x] += 1

#ans = 0
#for x, c in cnt.items():
#    ans += c * (c - 1)

#print(ans // 2)

        
