#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h() if m > 1 else typ(input()) for _ in range(n)]


def main():
    read_h()
    A = read_h()

    num_odd = 0
    for a in A:
        if a % 2 != 0:
            num_odd += 1

    if num_odd % 2 == 0:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
