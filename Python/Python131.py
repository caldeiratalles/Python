contador_pular = 1
lista = []
listaValor = []
listaNova = []
while contador_pular<13:
    inputs = input()
    contador_pular+=1
    if contador_pular == 2 or contador_pular == 5 or contador_pular == 8 or contador_pular == 11:
        contador_pular+=1
        inputs = (input())
        lista.append(inputs)
    if contador_pular == 3 or contador_pular == 6 or contador_pular == 9 or contador_pular == 12:
        contador_pular+=1
        inputs = int(input())
        listaValor.append(inputs)
nomes = {}
for letter in lista:
     nomes[letter] = nomes.get(letter,0) + 1

   


    
      
        
        