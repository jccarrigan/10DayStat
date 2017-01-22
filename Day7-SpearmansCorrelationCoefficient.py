from collections import OrderedDict as od

n, x, y = float(raw_input()), map(float, raw_input().split()), map(float, raw_input().split())
xod, yod = od(), od()

for i in range(int(n)):
    xod[x[i]] = 0
    yod[y[i]] = 0
    
sortx = sorted(x)
sorty = sorted(y)

rankx, ranky = 1, 1
for i in sortx:
    xod[i] = rankx
    rankx += 1
for j in sorty:
    yod[j] = ranky
    ranky += 1

d = []
for k in range(int(n)):
    d.append((xod.values()[k]-yod.values()[k])**2)
    
print round(1 - 6*sum(d)/(n*(n*n -1)), 3)
