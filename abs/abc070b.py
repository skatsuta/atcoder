#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h(typ) if m > 1 else typ(input()) for _ in range(n)]


def main():
    A, B, C, D = read_h()

    print(max(min(B, D) - max(A, C), 0))


if __name__ == '__main__':
    main()
