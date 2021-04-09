t = input()
t = int(t)
j = 0

while t>j:
    j = j+1
    if j%3==0 and not j%5==0:
        print('Fizz')
        continue
    if j%5==0 and not j%3==0:
        print('Buzz')
        continue
    if j%3==0 and j%5==0:
        print('Fizz Buzz')
        continue
    if not(j%3==0 and j%5==0):
        print(j)
            