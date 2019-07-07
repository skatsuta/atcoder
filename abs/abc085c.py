N, Y = map(int, input().split())


def search():
    for i in range(N + 1):
        for j in range(N - i + 1):
            k = N - i - j
            amount = 10000 * i + 5000 * j + 1000 * k
            if amount == Y:
                return (i, j, k)

    return (-1, -1, -1)


print(*search())
