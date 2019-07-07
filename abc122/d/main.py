import itertools as it

N = int(input().strip())

ss = it.product('ATGC', repeat=N)
cnt = 0
for s in ss:
    t = ''.join(s)

    if len(t) < 3:
        cnt += 1
        continue

    for i in range(len(t) - 2):
        u = t[i:i + 3]
        print(u)
        if 'AGC' not in u and 'ACG' not in u and 'GAC' not in u:
            cnt += 1

print(cnt)
