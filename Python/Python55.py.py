def imprimeTermos(n):
    n = n*-1
    if n%2 == 0:
         for i in range(n,1,2):
             print(i)
             
    else:
         for i in range(n,0,2):
             print(i)
             if i == -1:
                 print('0')
         