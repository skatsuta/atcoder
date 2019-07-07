#!/usr/bin/env python3


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, typ=int):
    return [typ(input()) for _ in range(n)]


def main():
    n, l = read_h()
    s = ''.join(sorted(read_v(n, typ=str)))
    print(s)


if __name__ == '__main__':
    main()
