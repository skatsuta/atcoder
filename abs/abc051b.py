#!/usr/bin/env python3


def read_h(typ=int):
    return map(typ, input().split())


def read_v(n, typ=int):
    return [typ(input()) for _ in range(n)]


def main():
    K, S = read_h()
    cnt = 0
    for x in range(K + 1):
        for y in range(min(S - x, K) + 1):
            z = S - x - y
            if z <= K:
                cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
