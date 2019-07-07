input()
d = [int(i) for i in input().split(' ')]
d = sorted(d)
N = len(d)
l, h = d[:N // 2], d[N // 2:]
ml = max(l)
mh = min(h)
print(mh - ml)
