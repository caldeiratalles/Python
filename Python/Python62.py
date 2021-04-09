import math
def acredita(n1,n2):
    base = 10
    t = ((math.log(n1,base))/(math.log(n2,base)))
    if n2**t==n1:
        return 'Pode Acreditar'
    else:
        return 'Fake News'