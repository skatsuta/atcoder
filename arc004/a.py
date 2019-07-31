#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)

# Override `input` function because `stdin.readline()` is 10x faster than built-in `input()`
input = sys.stdin.readline


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h(typ) if m > 1 else typ(input()) for _ in range(n)]


def main():
    n, = read_h()
    pts = read_v(n, m=2)

    from math import sqrt

    max_dist = 0.0
    for i in range(len(pts) - 1):
        for j in range(i + 1, len(pts)):
            x1, y1 = pts[i]
            x2, y2 = pts[j]
            dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
            max_dist = max(max_dist, dist)

    print(max_dist)


if __name__ == '__main__':
    main()
