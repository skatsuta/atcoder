#!/usr/bin/env python3


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h() if m > 1 else typ(input()) for _ in range(n)]


def main():
    N, K = read_h()
    A = read_h()

    cnt = [0] * (N + 1)
    for a in A:
        cnt[a] += 1

    ans = sum(sorted(cnt, reverse=True)[K:])
    print(ans)


if __name__ == '__main__':
    main()
