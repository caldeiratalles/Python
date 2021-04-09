n = int(input())
contador = 1
while contador<=n:
    movimento1,movimento2 = input().split()
    
    if movimento1=='tesoura' and movimento2=='pedra':
        
        print("Jogador 02 venceu.")
    if movimento1=='tesoura' and movimento2=='papel':
        print("Jogador 01 venceu.")
    if movimento1=='tesoura' and movimento2=='tesoura':
        print("Empate.")
    if movimento1=='pedra' and movimento2=='papel':
        print("Jogador 02 venceu.")
    if movimento1=='pedra' and movimento2=='tesoura':
        print("Jogador 01 venceu.")
    if movimento1=='pedra' and movimento2=='pedra':
        print("Empate.")
    if movimento1=='papel' and movimento2=='tesoura':
        print("Jogador 02 venceu.")
    if movimento1=='papel' and movimento2=='pedra':
        print("Jogador 01 venceu.")
    if movimento1=='papel' and movimento2=='papel':
        print("Empate.")
    contador +=1
 