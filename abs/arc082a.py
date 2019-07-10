#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h() if m > 1 else typ(input()) for _ in range(n)]


def main():
    N, = read_h()
    arr = read_h()

    cnts = [0] * 100000
    for a in arr:
        cnts[a] += 1

    ans = 0
    for i in range(len(cnts) - 2):
        c = cnts[i] + cnts[i + 1] + cnts[i + 2]
        if c > ans:
            ans = c

    print(ans)


if __name__ == '__main__':
    main()
