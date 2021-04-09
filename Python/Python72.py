popua, popub, cresa, cresb = (float(x) for x in input().split())
a = cresa/100
b = cresb/100
t = (popub - popua)/(popua*a - popub*b)
t = int(t)
print(t)
if t>=1000:
    print('Mais de um milenio.')
if 1<t<1000:
    print('Vai alcancar em',t,'ano(s).')
if t<0:
    print('A nunca alcancara B.')