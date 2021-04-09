def dinheiros(n,a,b): #a = 1 litro b = 2 litros
   if (b<a and n//2 < n//1 and b!=n):
     por_2 = n//2
     r = n%2
   
     por_1 = r//1
   
     func= por_2*b
     func1= por_1*a
     soma= func+func1
     print('%.0f'%soma)
   if b<a and n//2 > n//1 :
     por_2 = n//2
     r = n%2
   
     por_1 = r/1
   
     func= por_2*b
     func1= por_1*a
     soma= func+func1
     print('%.0f'%soma)
   if a==b:
        por_2 = n//2
        func= por_2*b
        print('%.0f'%func)
   if n==b:
        por_1 = n//1
        func= por_1*a
        print('%.0f'%func)
   if (b>a and n//2 < n//1) and (n!=b and b!=2):
     por_2 = n//2
     r = n%2
     if por_2 == 5:
           por_1 = n//1
           func1= por_1*a
           print(func1)
           
     else:
         por_1 = r//1
   
         func= por_2*b
         func1= por_1*a
         soma= func+func1
         print('%.0f'%soma)
   if b>a and n//2 > n//1 :
     por_2 = n//2
     r = n%2
   
     por_1 = r/1
   
     func= por_2*b
     func1= por_1*a
     soma= func+func1
     print('%.0f'%soma)
     
   
     
       
       