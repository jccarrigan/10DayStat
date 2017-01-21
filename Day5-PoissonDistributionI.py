import math

def factor(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factor(n-1)
    
mean, x = 2.5, 5

print ((mean**x)*math.exp(-mean))/(factor(x))
