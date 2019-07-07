#!/usr/bin/env python3

import math


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h() if m > 1 else typ(input()) for _ in range(n)]


def main():
    N, = read_h()

    ans = 100
    for a in range(1, int(math.sqrt(N)) + 1):
        if N % a != 0:
            continue

        b = N // a
        f = max(len(str(a)), len(str(b)))
        ans = min(ans, f)

    print(ans)


if __name__ == '__main__':
    main()
