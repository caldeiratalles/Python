def area(arg1,arg2,forma):
      
    if forma == 'losango':
        area = (arg1*arg2)/2
        print("O losango tem",'%.0f' % area,"de area")
    if forma == 'retangulo':
        area = (arg1*arg2)
        print("O retangulo tem",'%.0f' % area,"de area")
    if forma == 'triangulo':
        area = (arg1*arg2)//2
        print("O triangulo tem",'%.0f' % area,"de area")
    if forma == 'circulo':
        area = arg2 * (arg1**2)
        print("O circulo tem",'%.0f' % area,"de area")

