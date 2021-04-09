valor = int(input())
def função(valor):
    fatorial = 1
    while valor >=1:
        fatorial = fatorial * valor
        valor = valor -1
    print(fatorial)
    return 
função(valor)
