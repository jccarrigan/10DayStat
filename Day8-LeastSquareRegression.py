x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]
n = 5

def mean(l):
    return sum(l)/n

def std(l):
    sigmas = []
    mu = mean(l)
    for i in range(int(n)):
        sigmas.append((l[i]-mu)**2)
    return (sum(sigmas)/n)**0.5

def pearson(a, b, amu, bmu, astd, bstd):
    numer = []
    for i in range(int(n)):
        numer.append((a[i]-amu)*(b[i]-bmu))
    return sum(numer)/(n*astd*bstd)

xmu, ymu = mean(x), mean(y)
xstd, ystd = std(x), std(y)

B = pearson(x, y, xmu, ymu, xstd, ystd) * ystd/xstd
A = ymu - B*xmu

print round(A + 80*B, 3)
