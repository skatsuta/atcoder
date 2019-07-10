#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h() if m > 1 else typ(input()) for _ in range(n)]


def main():
    A, B, C = read_h()

    m3 = max(A, B, C) * 3
    sm = sum((A, B, C))
    if m3 % 2 == sm % 2:
        print((m3 - sm) // 2)
    else:
        print((m3 + 3 - sm) // 2)


if __name__ == '__main__':
    main()
