import sys
def sonho(n):
    x = input()
    x = int(x)
    contador = n+1
    print(contador)
    while x%2!=0:
        x = input()
        x = int(x)
        if x%2==0:
            contador = contador + 1
            print(contador)
            sys.exit()
        contador += 1 
        print(contador)
        
     
     