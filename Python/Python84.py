import sys
p = int(input())
string = input()
alfab = 'abcdefghijklmnopqrstuvwxyz'
cont = 0 #aumenta o contador caso der false
count2 = 0
c = -1
p = 0 
d = 0
while cont < len(alfab):
    c = string.find(alfab[p], c + 1)
    if len(string)==1:
        print(string)
        sys.exit()
        break
    if c >= 0 and p >= d:
        count2 = c
        d = p
    else:
        cont += 1
        p += 1
print (string[:count2] + string[count2+1:])
