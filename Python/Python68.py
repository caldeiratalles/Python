def three_Sum(num,valor):
    valor = int(valor)
    num1= []
    for str in num:
        for char in str:
            try:
                num = int(char)
                num1.append(num)
            except ValueError as verr:
                pass
    for i in range(len(num1)-2):
        left=i+1
        right=len(num1)-1
        if i!=0 and num1[i]==num1[i-1]:continue
        while True:
           func = num1[left]+num1[right]
           if func == valor:
               return print('E possivel ganhar.')
           else:
               return print('Impossivel ganhar.')
           
    
num = input().split()
valor = input()
three_Sum(num,valor)