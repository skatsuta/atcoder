#!/usr/bin/env python3


def read_h(typ=int):
    return map(typ, input().split())


def read_v(n, typ=int):
    return [typ(input()) for _ in range(n)]


def main():
    n = input()
    s = sum([int(d) for d in n])

    if int(n) % s == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
