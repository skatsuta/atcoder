input()
a = sorted(map(int, input().split()), reverse=True)

alice = sum(v for i, v in enumerate(a) if i % 2 == 0)
bob = sum(v for i, v in enumerate(a) if i % 2 != 0)

print(alice - bob)
