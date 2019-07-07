import heapq as hq

X, Y, Z, K = [int(n) for n in input().strip().split(' ')]
A = sorted([int(s) for s in input().strip().split(' ')], reverse=True)
B = sorted([int(s) for s in input().strip().split(' ')], reverse=True)
C = sorted([int(s) for s in input().strip().split(' ')], reverse=True)

q = []
i, j, k = 0, 0, 0
hq.heappush(q, (-(A[0] + B[0] + C[0]), i, j, k))
pushed = {(0, 0, 0)}

for _ in range(K):
    s, *idx = hq.heappop(q)
    idx = tuple(idx)

    print(-s)

    i, j, k = idx
    if i < X - 1 and (i + 1, j, k) not in pushed:
        hq.heappush(q, (-(A[i + 1] + B[j] + C[k]), i + 1, j, k))
        pushed.add((i + 1, j, k))
    if j < Y - 1 and (i, j + 1, k) not in pushed:
        hq.heappush(q, (-(A[i] + B[j + 1] + C[k]), i, j + 1, k))
        pushed.add((i, j + 1, k))
    if k < Z - 1 and (i, j, k + 1) not in pushed:
        hq.heappush(q, (-(A[i] + B[j] + C[k + 1]), i, j, k + 1))
        pushed.add((i, j, k + 1))
