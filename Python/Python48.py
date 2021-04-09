a , b , c = (int(x) for x in input().split())
def age(a,b,c):
    

    ano = a//360
    a = a - ano * 360

    mes = a//30
    a = a - mes*30

    dia = a
    
    
    anob = b//360
    b = b - anob * 360

    mesb = b//30
    b = b - mesb*30

    diab = b
    
    anoc = c//360
    c = c - anoc * 360

    mesc = c//30
    c = c - mesc*30

    diac = c
    print(ano,"ano(s),",mes,"mes(es) e",dia,"dia(s)")
    print(anob,"ano(s),",mesb,"mes(es) e",diab,"dia(s)")
    print(anoc,"ano(s),",mesc,"mes(es) e",diac,"dia(s)")
age(a , b , c)