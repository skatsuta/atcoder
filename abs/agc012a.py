#!/usr/bin/env python3


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, typ=int):
    return [typ(input()) for _ in range(n)]


def main():
    n, = read_h()
    a = sorted(read_h(), reverse=True)

    print(sum([ai for i, ai in enumerate(a[:2 * n]) if i % 2 == 1]))


if __name__ == '__main__':
    main()
