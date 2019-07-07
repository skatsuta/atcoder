#!/usr/bin/env python3


def read_h(conv=int):
    return map(conv, input().split())


def read_v(n, conv=int):
    return [conv(input()) for _ in range(n)]


def main():
    n = int(input())

    for i in range(n // 7 + 1):
        if (n - 7 * i) % 4 == 0:
            print('Yes')
            return

    print('No')


if __name__ == '__main__':
    main()
