import math
import sys

ts = [int(i) for i in sys.stdin.read().strip().split('\n')]
ds = [int(math.ceil(t / 10) * 10) - t for t in ts]
ans = sum(ts) + sum(ds) - max(ds)
print(ans)
