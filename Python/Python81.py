number_input = int(input())
contador = 1
while contador<=number_input:
    start,stop,word = input().split()
    start = int(start)
    stop = int(stop)
    a = word [start:(stop+1)]
    print(a)
    contador +=1

