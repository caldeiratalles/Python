def k_esimo(n,k):
    
    
    if n%2==0:
        
        if k>(n/2):
             valor=(2*(k-(n/2)))
             valor = int(valor)
             return valor
        if k==(n/2):
             valor=(n-1)
             valor = int(valor)
             return valor
             
        if k<(n/2):
             valor=(2*k)-1
             valor = int(valor)
             return valor
             
    if not n%2==0:
        if k>((n+1)/2):
            valor = 2*(k-((n+1)/2))
            valor = int(valor)
            return valor
        if k<(n/2):
             valor=(2*k)-1
             valor = int(valor)
             return valor
        if k==((n+1)/2):
             valor = n
             valor = int(valor)
             return valor
            
             
