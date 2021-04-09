import sys
a,b = input().split()
tamanho_b = len(a) - len(b) #7
if a==b:
    print('ta dentro!!!')
    sys.exit()
if len(a)==len(b) and a!=b:
    print('ta fora...')
    sys.exit()
if a[tamanho_b:]==b:
    print('ta dentro!!!')
    sys.exit()
if not a[tamanho_b:]==b:
    print('ta fora...')
    sys.exit()
