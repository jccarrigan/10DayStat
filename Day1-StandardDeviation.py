n, x, sigmas = float(input()), map(float, raw_input().split()), []

mean = sum(x)/n

for i in range(int(n)):
    sigmas.append((x[i]-mean)**2)
    
print round((sum(sigmas)/n)**0.5, 1)
