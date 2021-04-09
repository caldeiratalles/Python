popua, popub, cresa, cresb = (float(x) for x in input().split())
anos = 0
a = (cresa/100)
b = (cresb/100)
func1 = (popua*a)+ popua 
func1 = int(func1)


if ((cresa>cresb) and (func1>popua)) :
    while popua <= popub:
        popua = int(popua)
        popub = int(popub)
        popua = (popua) + ((popua * (a)))
        popub = (popub) + ((popub * (b)))
        anos += 1
    
        continue

if (anos>=1000 and popua>=popub):
    print('Mais de um milenio.')
        
if (popua>=popub and not anos>=1000):
    print('Vai alcancar em',anos,'ano(s).')
if not ((cresa>cresb) and (func1<popua)):
    print('A nunca alcancara B.')
    