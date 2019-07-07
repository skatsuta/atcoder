#!/usr/bin/env python3


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, typ=int):
    return [typ(input()) for _ in range(n)]


def main():
    n, k = read_h()
    l = sorted(read_h(), reverse=True)
    print(sum(l[:k]))


if __name__ == '__main__':
    main()
