N = int(input())


def f():
    tp, xp, yp = 0, 0, 0

    for _ in range(N):
        t, x, y = map(int, input().split())
        dt = t - tp
        dist = abs(x - xp) + abs(y - yp)

        if dist > dt or dist % 2 != dt % 2:
            return False

        tp, xp, yp = t, x, y

    return True


if f():
    print('Yes')
else:
    print('No')
