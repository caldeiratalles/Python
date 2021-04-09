a , b , c = (int(x) for x in input().split())
d , e , f = (int(x) for x in input().split())
g , h , i = (int(x) for x in input().split())

def resto (a, b, c):
 func = (a + b) % c
 print(func)
resto(a,b,c)
resto(d,e,f)
resto(g,h,i)