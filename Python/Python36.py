idade = input()
k = int(idade)

ano = k//365
k = k - ano * 365

mes = k//30
k = k - mes*30

dia = k

print(ano,"ano(s)")
print(mes,"mes(es)")
print(dia,"dia(s)")