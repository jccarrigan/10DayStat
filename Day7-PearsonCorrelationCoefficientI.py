n, x, y = float(raw_input()), map(float, raw_input().split()), map(float, raw_input().split())

def mean(l):
    return sum(l)/n

def std(l):
    sigmas = []
    mu = mean(l)
    for i in range(int(n)):
        sigmas.append((l[i]-mu)**2)
    return (sum(sigmas)/n)**0.5

xmu, ymu = mean(x), mean(y)
xstd, ystd = std(x), std(y)

numer = []
for i in range(int(n)):
    numer.append((x[i]-xmu)*(y[i]-ymu))
    
print round(sum(numer)/(n*xstd*ystd), 3)
