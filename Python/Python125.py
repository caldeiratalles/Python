inputs = int(input())
dic = {}
contador = 0
contadorr = 1
for i in range(inputs):
    conjunto = input().split(':')
    conjunto[1]= float(conjunto[1])
    if conjunto[1]>=5:
        a = dict([(conjunto[0],conjunto[1])])
        dic.update(a)
    else:
        continue
print(dic)
    