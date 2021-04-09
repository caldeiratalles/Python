inputs = input()
inputs = [ int(x) for x in inputs.split() ]
inputs = inputs[::-1]
inputs = tuple(inputs)
print(inputs)