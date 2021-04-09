
def triangulo(x,size): #
    x    = int(x)
    size = int(size)
    for i in range(size):
        k = ' ' * ((size//2) + x)
        t = k + (i + 1) * '+'
        size = size - 1
        if i % 2 == 0:
            print(t)
       

    
        
            
            
            
            
            