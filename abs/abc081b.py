import fractions
import math
from functools import reduce

input()
d = reduce(fractions.gcd, map(int, input().split()))
e = int(math.log2(d))
print(e)
