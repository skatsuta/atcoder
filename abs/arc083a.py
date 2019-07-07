#!/usr/bin/env python3


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h() if m > 1 else typ(input()) for _ in range(n)]


def main():
    a, b, c, d, e, f = read_h()

    conc_lim = 100 * e / (100 + e)
    print('conc lim', conc_lim)

    max_conc = 0.0
    ans = (0, 0)
    for wi in range(f // (100 * a) + 1):
        for wj in range(((f - a * wi) // (100 * b) + 1)):
            x = 100 * a * wi + 100 * b * wj
            print('x', x)

            for si in range((f - x) // c + 1):
                for sj in range((f - x - c * si) // d + 1):
                    y = c * si + d * sj
                    print('y', y)

                    if x + y == 0:
                        continue

                    conc = 100 * y / (x + y)
                    print('conc', conc)

                    if conc <= conc_lim and conc > max_conc:
                        max_conc = conc
                        print('max_conc', max_conc)
                        ans = (x + y, y)

                        if max_conc == conc_lim:
                            return

    print(*ans)


if __name__ == '__main__':
    main()
