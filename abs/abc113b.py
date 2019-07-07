n = input()
t, a = map(int, input().split())
H = map(int, input().split())

temp = [(i + 1, abs(a - (t - h * 0.006))) for i, h in enumerate(H)]
i = min(temp, key=lambda v: v[1])[0]
print(i)
