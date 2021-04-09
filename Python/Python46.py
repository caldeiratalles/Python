def qualPeriodo (m,a,s): # m = matricula a = ano s = semestre
    ano_entrou = m//10000000 # = 18 (ano que ele entrou)
    semestre_para_descobrir = m//100000  # = 1801 (para descobrir o semestre)
    senestre_entrou =  semestre_para_descobrir - (ano_entrou*100) # = 1(segundo) #semestre que ele entrou 0 primeiro 1 segundo
    anos_totais = (a-2000) - ano_entrou # = 2 anos
    
    semestres = anos_totais * 2 + s - senestre_entrou +1
    print(semestres)