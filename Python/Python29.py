n1 , n2 , n3 , n4 = input().split()

media = ((float(n1)*2) + (float(n2)*3) + (float(n3)*4) + (float(n4)*1))/10

if media >= 7:
    print("Media:",'%.1f' % media)
    print("Aluno aprovado.")
if media < 4.99:  
    print("Media:",'%.1f' % media)
    print("Aluno reprovado.")
if media >= 5.0  and media <= 6.9: 
    print("Media:",'%.1f' % media)
    print("Aluno em exame.")
    nota_do_exame = float(input())
    print("Nota do exame:",'%.1f' % nota_do_exame)
    new_media = (media + nota_do_exame)/2
    if new_media >= 5:
           print("Aluno aprovado.")
           print("Media final:",'%.1f' % new_media)
    if new_media <= 4.9 :
           print("Aluno reprovado.")
           print("Media final:",'%.1f' % new_media)