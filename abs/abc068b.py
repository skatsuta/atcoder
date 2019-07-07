n = int(input())
cnt = 0
ans = 1
for i in range(1, n + 1):
    c = 0
    rem = i
    while rem % 2 == 0:
        c += 1
        rem //= 2

    if c > cnt:
        cnt = c
        ans = i

print(ans)
