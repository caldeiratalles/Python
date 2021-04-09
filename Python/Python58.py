def sinuquera(n):
    if n%2==0 and n>0:
        
        divisão = (n//2) -1
        return divisão
    if not(n%2==0) and n>0:
        divisão = (n//2)
        return divisão
    if n<=0:
        
        return '0'
        