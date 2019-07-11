#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h() if m > 1 else typ(input()) for _ in range(n)]


def main():
    N, = read_h()
    A = read_v(N)

    cnts = {}
    for a in A:
        cnts[a] = cnts.get(a, 0) + 1

    #  print(cnts)

    ans = 0
    for n in cnts.values():
        if n % 2 != 0:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
