import math
import sys

n, *ns = [int(i) for i in sys.stdin.read().strip().split('\n')]
m = min(ns)

ans = math.ceil(n / m) + 4
print(ans)
