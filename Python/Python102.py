n = int(input())
lista = []
number = n
while number!=0:
    number = number-1
    if number==0:
        break
    if n%number==0:
       lista.append(number)
       continue
    else:
        number = number 
        continue

if sum(lista)==n:
    print(n,'eh perfeito')
else:
    print(n,'nao eh perfeito')
