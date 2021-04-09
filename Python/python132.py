def convert(l):
    nomes = {}
    listaKey = []
    listaValue = []
    for i in range(len(l)):
        if l[i][0] in listaKey:
            continue
        else:
           listaKey.append(l[i][0])
    contadorkey = 0
    for i in range(len(l)):
        listaValue = []
        for j in range(len(l)):
            if l[i][0] == l[j][0] and not (l[i][0] in nomes):
                listaValue.append(l[j][1])
        if listaValue == []:
            continue
        else:
            nomes[listaKey[contadorkey]] = listaValue
        contadorkey+=1
    return nomes

    
    
    
    
    
