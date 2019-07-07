#!/usr/bin/env python3


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h() if m > 1 else typ(input()) for _ in range(n)]


def main():
    A, B, C, X, Y = read_h()

    base_cnt = min(X, Y)
    ans = min(A + B, C * 2) * base_cnt + (X - base_cnt) * min(A, C * 2) + \
        (Y - base_cnt) * min(B, C * 2)
    print(ans)


if __name__ == '__main__':
    main()
