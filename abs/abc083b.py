N, A, B = map(int, input().split())

total = 0
for n in range(1, N + 1):
    sm = sum(int(s) for s in str(n))
    if A <= sm and sm <= B:
        total += n

print(total)
