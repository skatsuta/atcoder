#!/usr/bin/env python3


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, typ=int):
    return [typ(input()) for _ in range(n)]


def main():
    n, x = read_h()
    a = sorted(read_h())

    cnt = 0
    rem = x
    for ai in a:
        rem -= ai
        if rem < 0:
            break
        cnt += 1

    if rem > 0:
        cnt -= 1

    print(cnt)


if __name__ == '__main__':
    main()
