k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
i = 1
n_drag_apanharam = 0
while i <= d:
    if (((i % k) != 0) and ((i % l) != 0) and ((i % m) != 0) and ((i % n) != 0)):
             n_drag_apanharam = n_drag_apanharam + 1
    i = i+1
n_drag_apanharam = d - n_drag_apanharam       
print(n_drag_apanharam)