n, x, w = input(), map(float, raw_input().split()), map(float, raw_input().split())
print round(sum([x[i] * w[i] for i in range(n)])/sum(w), 1)
