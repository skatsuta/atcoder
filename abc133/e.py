#!/usr/bin/env python3


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h() if m > 1 else typ(input()) for _ in range(n)]


MOD = 10**9 + 7


def dfs(colors, graph, parent, current):
    if colors < len(graph[current]):
        return 0

    num_avail_colors = colors - 1 if parent < 0 else colors - 2
    num_cases = 1
    neighbors = graph[current]
    for neighbor in neighbors:
        if neighbor == parent:
            continue

        num_cases *= num_avail_colors
        num_avail_colors -= 1
        num_cases %= MOD

    for neighbor in neighbors:
        if neighbor == parent:
            continue

        num_cases *= dfs(colors, graph, current, neighbor)
        num_cases %= MOD

    return num_cases


def main():
    N, K = read_h()
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = read_h()
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    ans = K * dfs(K, graph, -1, 0) % MOD
    print(ans)


if __name__ == '__main__':
    main()
