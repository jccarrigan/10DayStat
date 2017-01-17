n, x, f, s = input(), map(int, raw_input().split()), map(int, raw_input().split()), []

for i in range(n):
    for _ in range(f[i]):
        s.append(x[i])

s.sort()
N = len(s)

if N % 2 == 0:
    u = s[(N/2):]
    l = s[:(N/2)]
elif N % 2 != 0:
    u = s[((N/2)+1):]
    l = s[:(N/2)]

def median(arr):
    if len(arr) % 2 != 0:
#        print 'odd', arr[len(arr)/2]
        return float(arr[len(arr)/2])
    else:
#        print 'even', arr[len(arr)/2], arr[(len(arr)/2)-1]
        return (float(arr[len(arr)/2]) + float(arr[(len(arr)/2)-1]))/2.0

print median(u) - median(l)
