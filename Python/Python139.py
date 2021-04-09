a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

def maior(a,b,c):
    lista = []
    funçãoab = (a+b+abs(a-b))/2
    funçãoac = (a+c+abs(a-c))/2
    funçãobc = (b+c+abs(b-c))/2
    lista.append(funçãoab)
    lista.append(funçãoac)
    lista.append(funçãobc)
    print(int(max(lista)),'eh o maior')
    return
maior(a,b,c)
    