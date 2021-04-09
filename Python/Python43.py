s1 , s2 , s3 = (str(x) for x in input().split())
s3 = int(s3)


def concatenar(s1,s2):
    func = s1 + s2
    print(func)
def repetir(s1,s3):
    
    func = s1 * s3
    print(func)
def ambos(s1 , s2, s3):
    
    func = (s1 + s2) * s3
    print(func)

concatenar(s1,s2)
repetir(s1,s3)
ambos(s1 , s2, s3)