#!/usr/bin/env python3


def read_h(conv=int):
    return map(conv, input().split())


def read_v(n, conv=int):
    return [conv(input()) for _ in range(n)]


n, x = read_h()
m = read_v(n)

print(len(m) + (x - sum(m)) // min(m))
