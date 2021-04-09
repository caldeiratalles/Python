import sys
x = input()
x = int(x)
def maravilhosos(x):
    
    if x==1:
        print(x)
        sys.exit()
        
    else:
     print(x)
     while x!=1:
         
        if x%2 == 0 and  x!=1:    
          func1 = x//2
          x = func1
          print(func1)
          continue
        if not x%2 == 0 and x!=1:
            func2 = 3*x +1
            x = func2
            print(func2)
            continue
maravilhosos(x)        
    
        
                   
        
                   
    
         
            
            
