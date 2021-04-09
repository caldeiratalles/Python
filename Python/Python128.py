valor = int(input())
dic = {}
for i in range(1,(valor+1)):
    if i%2==0:
        a = i*i
        dic[i] = a
    else:
        a = 5*i
        dic[i] = a
print(dic)
    