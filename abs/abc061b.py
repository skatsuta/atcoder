#!/usr/bin/env python3


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [tuple(map(typ, input().split())) if m > 1 else typ(input()) for _ in range(n)]


def main():
    N, M = read_h()
    roads = read_v(M, m=2)
    cnt = [0] * N

    for a, b in roads:
        cnt[a - 1] += 1
        cnt[b - 1] += 1

    for c in cnt:
        print(c)


if __name__ == '__main__':
    main()
