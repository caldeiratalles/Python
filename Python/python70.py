import statistics
t = []
while True:
    a = input()
    a = int(a)
    if a == -1:
        func = statistics.mean(t)
        print(int(func))
        break
    t.append(a)
    