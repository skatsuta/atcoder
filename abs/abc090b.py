#!/usr/bin/env python3


def read_h(typ=int):
    return map(typ, input().split())


def read_v(n, typ=int):
    return [typ(input()) for _ in range(n)]


def main():
    a, b = read_h()
    cnt = 0
    for i in range(a, b + 1):
        s = str(i)
        if s[:2] == s[3:][::-1]:
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
