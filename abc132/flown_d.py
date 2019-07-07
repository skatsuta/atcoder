N, K = map(int, input().split(' '))
MOD = 10**9 + 7

n = N - K + 1
print(n)
for i in range(2, K + 1):
    n = (n * (N - K + 2 - i) * (K - i + 1) // (i * (i - 1)))
    print(n % MOD)
