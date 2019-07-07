#!/usr/bin/env python3

from math import hypot


def read_h(typ=int):
    return map(typ, input().split())


def read_v(n, typ=int):
    return [typ(input()) for _ in range(n)]


def main():
    n = int(input())
    pts = [tuple(map(int, input().split())) for _ in range(n)]

    ans = 0.0
    for i, (x1, y1) in enumerate(pts):
        for (x2, y2) in pts[i:]:
            dist = hypot(x1 - x2, y1 - y2)
            if dist > ans:
                ans = dist

    print(ans)


if __name__ == '__main__':
    main()
