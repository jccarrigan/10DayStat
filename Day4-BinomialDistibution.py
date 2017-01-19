b, g = list(map(float, raw_input().split(" ")))
odds = b/g

def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)
    
print round(sum([b(i, 6, odds / (1 + odds)) for i in range(3, 7)]), 3)
