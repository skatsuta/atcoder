#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h(typ) if m > 1 else typ(input()) for _ in range(n)]


MOD = 10**9 + 7


def main():
    N, = read_h()

    ans = 1
    for i in range(1, N + 1):
        ans *= i
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
