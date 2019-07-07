#!/usr/bin/env python3


def read_h(typ=int):
    return map(typ, input().split())


def read_v(n, typ=int):
    return [typ(input()) for _ in range(n)]


def digit_sum(i):
    return sum([int(d) for d in str(i)])


def main():
    n, = read_h()
    ans = 10000
    for a in range(1, n):
        b = n - a
        s = digit_sum(a) + digit_sum(b)
        if s < ans:
            ans = s

    print(ans)


if __name__ == '__main__':
    main()
