def is_imperfect(n):
    count=0
    for val in range(1,n):
        if n % val == 0:
            count += val
            
    if count==n:
        return False
    else:
        return True