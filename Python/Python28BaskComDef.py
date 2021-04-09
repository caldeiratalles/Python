import math
def d(a,b,c):
    dels = b*b - 4*a*c
    return dels

def tudo(a,b,c,d):
   delta = d(a,b,c)
   
   if delta<0:
 
         d1 = delta * -1
         raiz1 = (((-b) + (math.sqrt(d1)))/(2*a))
         raiz2 = (((-b) - (math.sqrt(d1)))/(2*a))
         print('Primeira raiz ',raiz1,'*i e segunda raiz',raiz2,'*i')
         input

   else:

       raizn1 = (((-b) + (math.sqrt(d)))/(2*a))
       raizn2 = (((-b) + (math.sqrt(d)))/(2*a))

       print('Os valores da raiz são',raizn1,'e',raizn2)
       return print



tudo(a, b, c, d)
   





    