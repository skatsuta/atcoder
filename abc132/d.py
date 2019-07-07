def binomial(n, k):
    if n < k:
        return 0

    n2, k2 = 1, 1
    for i in range(1, min(k, n - k) + 1):
        n2 *= n
        k2 *= i
        n -= 1
    return n2 // k2


mod = 10**9 + 7
N, K = map(int, input().split())
for i in range(1, K + 1):
    a = binomial(N - K + 1, i) * binomial(K - 1, i - 1)
    print(a % mod)
