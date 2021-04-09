def stockmarket(stock):
    nomes = {}
    listaKey = []
    listaValue = []
    for i in range(len(stock)):
        if stock[i][0] in listaKey:
            continue
        else:
           listaKey.append(stock[i][0])
    contadorkey = 0
    for i in range(len(stock)):
        listaValue = []
        for j in range(len(stock)):
            if stock[i][0] == stock[j][0] and not (stock[i][0] in nomes):
                listaValue.append(float(stock[j][1]*stock[j][2]))
        if listaValue == []:
            continue
        else:
            nomes[listaKey[contadorkey]] = sum(listaValue)
        contadorkey+=1
    return nomes

    
