X, Y, Z, K = [int(n) for n in input().strip().split(' ')]
A = sorted([int(s) for s in input().strip().split(' ')], reverse=True)
B = sorted([int(s) for s in input().strip().split(' ')], reverse=True)
C = sorted([int(s) for s in input().strip().split(' ')], reverse=True)

ABC = []
for i, a in enumerate(A):
    for j, b in enumerate(B):
        if (i + 1) * (j + 1) > K:
            break

        for k, c in enumerate(C):
            if (i + 1) * (j + 1) * (k + 1) > K:
                break

            ABC.append(a + b + c)

ABC.sort(reverse=True)

for s in ABC[:K]:
    print(s)
