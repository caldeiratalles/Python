n = int(input())
w = n
k = 0
while True:
    condicao= int(input())
    if condicao==-1:
        print('Lar Deivis lar')
        break
    if condicao == 0:
        n = n -1
        if n <0:
            while True:
                j = int(input())
                if j==-1:
                    print(k)
                    break
            break
        k = k+1
    if condicao==1:
        gasolina_mais = int(input())
        if gasolina_mais+n>w:
            n = w
            k = k+1
            continue
        if not gasolina_mais+n>w:
            n = gasolina_mais + n
            k = k+1
            continue
    if condicao==2:
        gasolina_menos = int(input())
        if n - gasolina_menos<0:
            while True:
                j = int(input())
                if j==-1:
                    print(k)
                    break
            break
        else:
            n = n-gasolina_menos
            k = k+1
            continue
                
    
            
        
    


        