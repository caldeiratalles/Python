N = int(input())
 
for i in range(N):
    line = input()
    line = [h for h in line]
 
    j = 0
    tam = (len(line))
    line_aux = list()
    line_aux_w = list()
 
    while j < tam:
        if line[j].isupper():
            line_aux_w.append(line[j])
        
        j+=1
 
    j = 0
 
    while j < tam:
        num = str()
 
        while line[j] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            num += line[j]  
            j+=1
        
            if j == tam:
                break
 
        line_aux.append(num)    
 
        j+=1
 
    line_aux.remove('')
    line_aux = [int(j) for j in line_aux]
    j = 0
 
    while j < len(line_aux):
        print(line_aux_w[j]*line_aux[j], end='')
        j+=1
 
    print()