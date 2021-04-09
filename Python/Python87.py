number_inputs = int(input())
contadorLetra = 0
contadornumero = 1
listaPrin = []
C_Paradadeletras = 0
numbers = ['1','2','3','4','5','6','7','8','9','0']
alfabeto = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
a = input()
while number_inputs:
    if (a[contadorLetra] in alfabeto):
        if (a[contadornumero] in numbers):
            if not (contadornumero+1)>=len(a):
                  if (a[(contadornumero+1)] in numbers):
                      multi = a[contadornumero:(contadornumero+1+1)]
                      multi = int(multi)
                      string = a[contadorLetra]*multi
                      listaPrin.append(string)
                      contadorLetra+=3
                      contadornumero+=3
                  else:
                    multi = a[contadornumero:contadornumero+1]
                    multi = int(multi)
                    string = a[contadorLetra]*multi
                    listaPrin.append(string)
                    contadorLetra+=2
                    contadornumero+=2
 
            else:
                multi = a[contadornumero:contadornumero+1]
                multi = int(multi)
                string = a[contadorLetra]*multi
                listaPrin.append(string)
                contadorLetra+=2
                contadornumero+=2
        
        
                
            
                

            
        
