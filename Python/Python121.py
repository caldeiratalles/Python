contador = 0
somador = 0
contador_positivo = 0
while contador!=6:
    valor = float(input())
    if valor>0:
        somador = valor + somador
        contador_positivo+=1
        contador+=1
        continue
    if valor<0:
        contador+=1
        continue
print(contador_positivo,'valores positivos')
print(somador/contador_positivo)


