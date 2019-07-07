#!/usr/bin/env python3


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, typ=int):
    return [typ(input()) for _ in range(n)]


def main():
    S = input()

    for i in range(26):
        c = chr(ord('a') + i)
        if c not in S:
            print(c)
            return

    print(None)


if __name__ == '__main__':
    main()
