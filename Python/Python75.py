def ehPrimo(n):
    cont = 0
    i = 0

    while i <= n or cont < 2:
        
        
        i = i + 1
        x = n % i
    if x == 0:
        cont = cont + 1

    if cont <= 2:
        
        return print("1")
    else:
        return print("0")
      
    


        







        
