from collections import Counter
N, arr = input(), sorted(map(int, raw_input().split()))

print sum(arr)/float(N)

if N % 2 == 0:
    print (float(arr[N/2]) + float(arr[N/2 - 1]))/2.0
else: 
    print float(arr[N/2])
    
counted = Counter(arr)
max_value = sorted(counted.values())[-1]
print sorted([i for i in counted.keys() if counted[i] == max_value])[0]   
