a , b , c = (int(x) for x in input().split())
d = {a,b,c}
def age(d):
    

    ano = d//360
    d = d - ano * 360

    mes = d//30
    d = d - mes*30

    dia = d
    
    
    
    print(ano,mes,dia)
    
    
age(d)

