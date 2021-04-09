codigo1, numero_de_pecas1 , valor1 = input().split()
codigo2, numero_de_pecas2, valor2 = input().split()

total_a_pagar = ((float(numero_de_pecas1)) * float((valor1))) + (float(numero_de_pecas2)*float((valor2)))

print("VALOR A PAGAR: R$",'%.2f' % total_a_pagar)
