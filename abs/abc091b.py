#!/usr/bin/env python3


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [tuple(map(typ, input().split())) if m > 1 else typ(input()) for _ in range(n)]


def main():
    N, = read_h()
    s = read_v(N, typ=str)
    M, = read_h()
    t = read_v(M, typ=str)

    cnt = {}
    for si in s:
        cnt[si] = cnt.get(si, 0) + 1
    for ti in t:
        cnt[ti] = cnt.get(ti, 0) - 1

    ans = max(0, *cnt.values())
    print(ans)


if __name__ == '__main__':
    main()
