# Initialization
N, M = map(int, input().split())
adj = {}
for _ in range(M):
    u, v = [int(i) - 1 for i in input().split()]
    if u in adj:
        adj[u].append(v)
    else:
        adj[u] = [v]
S, T = [int(i) - 1 for i in input().split()]

INF = -1
dist = [[INF] * 3 for _ in range(N)]

# BFS
q = [(S, 0)]
dist[S][0] = 0
while q:
    u, nl = q.pop(0)
    if u not in adj:
        continue
    for v in adj[u]:
        ml = (nl + 1) % 3
        if dist[v][ml] != INF:
            continue
        dist[v][ml] = dist[u][nl] + 1
        q.append((v, ml))

ans = dist[T][0]
if ans == INF:
    print(-1)
else:
    print(ans // 3)
