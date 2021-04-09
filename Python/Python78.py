a = int (input())
n = a
k = 0
if n > 0:
    while n >= 0:
        print (n, end=" ")
        n = n - 2
        if n < 0:
            print ("\n", end="")
            k = k + 2
            n = a - k
