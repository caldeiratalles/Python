def piscininha (x,y,w,h,a,b):
    x_w = (x+w)
    y_h = (y+h)
    if x<a<x_w and y<b<y_h:
        print("Dando um tchibum")
    if ((x<=a<=x_w) and (b==y or b==y_h)) or ((y<=b<=y_h) and (a==x or a==x_w)):
        print("So com os pezin dentro da agua")
    
    if  (a>x_w or b>y_h) or (a<x or b<y):
        print("Tomando um solzin")
   
        
       
     