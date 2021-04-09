import statistics
n,a = input().split()
n = int(n)
a = int(a)
b = 0
t = []
while n>b:
    b = b+1
    c = input()
    c = int(c)
    t.append(c) #add nessa lista vazia.append(os termos desse)
media = statistics.mean(t) 
if media==a or media>a:
    print('media:',int(media))
    print('o rock reinara mais uma vez')
if media<=a:
    print('media:',int(media))
    print('rockeiros trabalhando ja')
    
    