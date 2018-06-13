def add(m,n):
    if n == 0:
        return m
    else:
        return add(m,n-1) + 1
    
def mult(m, n):
    if n == 0:
        return 0
    else:
        return mult(m, n-1) + m
    
def power(x, n):
    if n == 0:
        return 1
    else:
        return power(x, n-1) * x
    
print ("Adding:", add(5, 3))
print("Multiplying:", mult(8, 3))
print("Raise to power:", power(6, 4))
