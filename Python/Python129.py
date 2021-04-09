string = input()

# Recebendo histograma
dicio = dict()
for t in string:
    if t not in dicio:
        dicio[t] = 1
    else:
        dicio[t] += 1
print(dicio)
# invertendo o histograma
dicioInver = dict()
for string in dicio:
    if dicio[string] not in dicioInver:
        dicioInver[dicio[string]] = string # pego a palavra e associo com o numero
    else: # se ja tiver um numero some como string as variaveis
        dicioInver[dicio[string]] = dicioInver[dicio[string]]+string
for string in dicio:
    dicioInver[dicio[string]] = list(dicioInver[dicio[string]])# o metodo list tira esses espaços
print(dicioInver)
