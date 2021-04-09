import math
k = int(input())
n_cogumelostrain, n_cogumelostest = input().split()
n_cogumelostrain = int(n_cogumelostrain)
n_cogumelostest = int(n_cogumelostest)
matriz_em_forma_numero1 = [] #matriz trocado os caracteres por numeros
matriz_em_forma_numero2 = [] #matriz dos testes trocado os caracteres por numeros
matriz_em_relação_PE = []
def media(n_cogumelostrain):
    contador = 0
    listaprovi = 0
    subconjunto = 0
    elemento = 0
    matriz_passo1_media = []
    while True:
        
        while True:
            listaprovi += matriz_em_forma_numero1[subconjunto][elemento] 
            subconjunto+=1
            if subconjunto == n_cogumelostrain:
                break
            
        matriz_passo1_media.append((listaprovi/n_cogumelostrain))
        if elemento == 21:
            break
        elemento+=1
        subconjunto = 0
        listaprovi = 0
    
    return matriz_passo1_media
#somar a linha 1 com a 2 em diante em loop lembrar que tem subconjuntos então []#primeiro conjunto[]#primeiro elemento do subconjunto
def DesvioPadrão(matriz_passo1_media):
    desvio_padrao = []
    soma = 0
    for j in range(22):
        for i in range(n_cogumelostrain):
            soma += ((matriz_em_forma_numero1[i][j] - matriz_passo1_media[j])**2)
        soma = math.sqrt((soma/n_cogumelostrain))
        desvio_padrao.append(soma)
        soma = 0
    
    return desvio_padrao
def normalizacao(desvio_padrao):
    normalizacao = []
    for i in range(n_cogumelostrain):
        sub1 = []
        for j in range(22):
             if desvio_padrao[j] > 0:
                 sub = ((matriz_em_forma_numero1[i][j] - matriz_passo1_media[j]))/desvio_padrao[j] 
             else:
                 sub = 0
             sub1.append(sub)
        normalizacao.append((sub1))
    return normalizacao
#Trocar as caracteristicas por numeros
numero_caracteristica =  [['b', 'c', 'x', 'f', 'k', 's'], ['f', 'g', 'y', 's'], ['n', 'b', 'c', 'g', 'r', 'p', 'u', 'e', 'w', 'y'], ['t', 'f'], ['a', 'l', 'c', 'y', 'f', 'm', 'n', 'p', 's'], ['a', 'd', 'f', 'n'] , ['c', 'w', 'd'], ['b', 'n'], ['k', 'n', 'b', 'h', 'g', 'r', 'o', 'p', 'u', 'e', 'w', 'y'], ['e', 't'], ['b', 'c', 'u', 'e', 'z', 'r', '?'], ['f', 'y', 'k', 's'], ['f', 'y', 'k', 's'], ['n', 'b', 'c', 'g', 'o', 'p', 'e', 'w', 'y'], ['n', 'b', 'c', 'g', 'o', 'p', 'e', 'w', 'y'], ['p', 'u'], ['n', 'o', 'w', 'y'], ['n', 'o', 't'], ['c', 'e', 'f', 'l', 'n', 'p', 's', 'z'], ['k', 'n', 'b', 'h', 'r', 'o', 'u', 'w', 'y'], ['a', 'c', 'n', 's', 'v', 'y'], ['g', 'l', 'm', 'p', 'u', 'w', 'd']]
contador = 0
while True:
    contadorwhile1 = 0
    contador2while = 0
    numero_caracteristica =  [['b', 'c', 'x', 'f', 'k', 's'], ['f', 'g', 'y', 's'], ['n', 'b', 'c', 'g', 'r', 'p', 'u', 'e', 'w', 'y'], ['t', 'f'], ['a', 'l', 'c', 'y', 'f', 'm', 'n', 'p', 's'], ['a', 'd', 'f', 'n'] , ['c', 'w', 'd'], ['b', 'n'], ['k', 'n', 'b', 'h', 'g', 'r', 'o', 'p', 'u', 'e', 'w', 'y'], ['e', 't'], ['b', 'c', 'u', 'e', 'z', 'r', '?'], ['f', 'y', 'k', 's'], ['f', 'y', 'k', 's'], ['n', 'b', 'c', 'g', 'o', 'p', 'e', 'w', 'y'], ['n', 'b', 'c', 'g', 'o', 'p', 'e', 'w', 'y'], ['p', 'u'], ['n', 'o', 'w', 'y'], ['n', 'o', 't'], ['c', 'e', 'f', 'l', 'n', 'p', 's', 'z'], ['k', 'n', 'b', 'h', 'r', 'o', 'u', 'w', 'y'], ['a', 'c', 'n', 's', 'v', 'y'], ['g', 'l', 'm', 'p', 'u', 'w', 'd']]
    caracteristica_cogumelotrain = input().split()
    while contadorwhile1 != 22:
        contador2while = 0
        while contador2while != len(numero_caracteristica[contadorwhile1]):
            if numero_caracteristica[contadorwhile1][contador2while] == caracteristica_cogumelotrain[contadorwhile1]:
                caracteristica_cogumelotrain[contadorwhile1] = contador2while
            else:
                contador2while+=1
        contadorwhile1 +=1
    matriz_em_forma_numero1.append(caracteristica_cogumelotrain)
    contador+=1
    if contador == n_cogumelostrain:
        break


#troquei as caracteristicas por numero e salvei numa lista.
contadorRotulo = n_cogumelostrain
while contadorRotulo > 0:
    tipo = input()
    matriz_em_relação_PE.append(tipo)
    contadorRotulo -= 1

numero_caracteristica =  [['b', 'c', 'x', 'f', 'k', 's'], ['f', 'g', 'y', 's'], ['n', 'b', 'c', 'g', 'r', 'p', 'u', 'e', 'w', 'y'], ['t', 'f'], ['a', 'l', 'c', 'y', 'f', 'm', 'n', 'p', 's'], ['a', 'd', 'f', 'n'] , ['c', 'w', 'd'], ['b', 'n'], ['k', 'n', 'b', 'h', 'g', 'r', 'o', 'p', 'u', 'e', 'w', 'y'], ['e', 't'], ['b', 'c', 'u', 'e', 'z', 'r', '?'], ['f', 'y', 'k', 's'], ['f', 'y', 'k', 's'], ['n', 'b', 'c', 'g', 'o', 'p', 'e', 'w', 'y'], ['n', 'b', 'c', 'g', 'o', 'p', 'e', 'w', 'y'], ['p', 'u'], ['n', 'o', 'w', 'y'], ['n', 'o', 't'], ['c', 'e', 'f', 'l', 'n', 'p', 's', 'z'], ['k', 'n', 'b', 'h', 'r', 'o', 'u', 'w', 'y'], ['a', 'c', 'n', 's', 'v', 'y'], ['g', 'l', 'm', 'p', 'u', 'w', 'd']]
contador = 0
#trocar caracteristicas do test
while True:
    contadorwhile1 = 0
    contador2while = 0
    numero_caracteristica =  [['b', 'c', 'x', 'f', 'k', 's'], ['f', 'g', 'y', 's'], ['n', 'b', 'c', 'g', 'r', 'p', 'u', 'e', 'w', 'y'], ['t', 'f'], ['a', 'l', 'c', 'y', 'f', 'm', 'n', 'p', 's'], ['a', 'd', 'f', 'n'] , ['c', 'w', 'd'], ['b', 'n'], ['k', 'n', 'b', 'h', 'g', 'r', 'o', 'p', 'u', 'e', 'w', 'y'], ['e', 't'], ['b', 'c', 'u', 'e', 'z', 'r', '?'], ['f', 'y', 'k', 's'], ['f', 'y', 'k', 's'], ['n', 'b', 'c', 'g', 'o', 'p', 'e', 'w', 'y'], ['n', 'b', 'c', 'g', 'o', 'p', 'e', 'w', 'y'], ['p', 'u'], ['n', 'o', 'w', 'y'], ['n', 'o', 't'], ['c', 'e', 'f', 'l', 'n', 'p', 's', 'z'], ['k', 'n', 'b', 'h', 'r', 'o', 'u', 'w', 'y'], ['a', 'c', 'n', 's', 'v', 'y'], ['g', 'l', 'm', 'p', 'u', 'w', 'd']]
    caracteristica_cogumelottest = input().split()

    while contadorwhile1 != 22:
        contador2while = 0
        while contador2while != len(numero_caracteristica[contadorwhile1]):
            if numero_caracteristica[contadorwhile1][contador2while] == caracteristica_cogumelottest[contadorwhile1]:
                caracteristica_cogumelottest[contadorwhile1] = contador2while
            
            else:
                contador2while+=1
        contadorwhile1 +=1
    matriz_em_forma_numero2.append(caracteristica_cogumelottest)
    contador+=1
    if contador == n_cogumelostest:
        break

 
#chamar as funções
matriz_passo1_media = media(n_cogumelostrain)
desvio_padrao = DesvioPadrão(matriz_passo1_media)
normalizacao = normalizacao(desvio_padrao)
########################
#normalizacao do caso de teste
normalizacao1 = []
for i in range(n_cogumelostest):
    sub1 = []
    for j in range(22):
         if desvio_padrao[j] > 0:
             sub = ((matriz_em_forma_numero2[i][j] - matriz_passo1_media[j]))/desvio_padrao[j] 
         else:
             sub = 0
         sub1.append(sub)
    normalizacao1.append((sub1))
# inicio do calculo da distância euclediana
#for x in range(n_cogumelostest):
#   lista_de = []
#   contadorrr = 0
#   for i in range (n_cogumelostrain):
#       somar_termo_passado = 0
#        for j in range (22):
#            valor = (normalizacao1[x][j] - normalizacao[i][j])**2 
#            somar_termo_passado += valor
#        somar_termo_passado = somar_termo_passado**(1/2) # fim do calculo
#        somar_termo_passado = [somar_termo_passado,matriz_em_relação_PE[contadorrr]] #atribuir P e E pra contagem
#        contadorrr+=1 # variar o P e E
#        lista_de.append(somar_termo_passado)
i = 0
x = 0
j = 0
lista_de = []
contadorrr = 0
somar_termo_passado = 0
while x<n_cogumelostest:
    
    valor = (normalizacao1[x][j] - normalizacao[i][j])**2 #O x nunca vai zerar,o J zera nos dois e o I só varia quando o j==22 e no segundo if pra confirmar
    somar_termo_passado += valor
    j+=1
    if j==22:
        i+=1
        a = math.sqrt(somar_termo_passado)
        lista_de.append((a,matriz_em_relação_PE[contadorrr]))
        contadorrr+=1
        j = 0
        somar_termo_passado = 0
    if i==n_cogumelostrain:
        #varrer a lista e contar os P's e os E's
        lista_de.sort()
        print(lista_de)
        while True:
            contador_varredura = 0
            contadorP = 0
            contadorE = 0
            lista_de.sort()
            while contador_varredura<k:
                if lista_de[contador_varredura][1]=='p': 
                    contadorP+=1
                    contador_varredura+=1
                else:
                    contadorE+=1
                    contador_varredura+=1
            if contadorP>contadorE:
                print('p')
                break
            else:
                print('e')
                break
        i = 0
        j = 0
        lista_de = []
        contadorrr = 0
        somar_termo_passado = 0
        x+=1


            

