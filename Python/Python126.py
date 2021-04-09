inputs = int(input())
dic = {}
for i in range(inputs):
    string = input().split(':')
    a = dict([(string[0],string[1])])
    print(a)
    dic.update(a)
print(dic)
    