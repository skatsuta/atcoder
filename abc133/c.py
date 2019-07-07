#!/usr/bin/env python3


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h() if m > 1 else typ(input()) for _ in range(n)]


def main():
    L, R = read_h()

    if R - L >= 2019 or R % 2019 <= L % 2019:
        print(0)
        return

    ans = 2019
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            ans = min(ans, (i % 2019) * (j % 2019) % 2019)

    print(ans)


if __name__ == '__main__':
    main()
