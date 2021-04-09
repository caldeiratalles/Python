n = int(input('Escolha o valor da sequência de Fibonacci até 60:'))
i = 0
ultimo = 1
penultimo = 1
for valor in range(2,n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        valor += 1
print(termo)