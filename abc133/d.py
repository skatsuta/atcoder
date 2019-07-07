#!/usr/bin/env python3


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h() if m > 1 else typ(input()) for _ in range(n)]


def main():
    N, = read_h()
    A = read_h()

    x1 = sum(A) - 2 * sum(a for i, a in enumerate(A) if i % 2 != 0)
    ans = [x1]

    for i in range(N - 1):
        ans.append(2 * A[i] - ans[i])

    print(*ans)


if __name__ == '__main__':
    main()
