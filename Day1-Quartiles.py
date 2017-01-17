n, x = input(), sorted(map(int, raw_input().split()))
if n % 2 == 0:
    u = x[(n/2):]
    l = x[:(n/2)]
elif n % 2 != 0:
    u = x[((n/2)+1):]
    l = x[:(n/2)]

def median(arr):
    if len(arr) % 2 != 0:
#        print 'odd', arr[len(arr)/2]
        return arr[len(arr)/2]
    else:
#        print 'even', arr[len(arr)/2], arr[(len(arr)/2)-1]
        return (arr[len(arr)/2] + arr[(len(arr)/2)-1])/2

print median(l)
print median(x)
print median(u)
