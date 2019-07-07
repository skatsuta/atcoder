string = input().strip()

longest = 0
current = 0

for s in string:
    if s in ('A', 'T', 'G', 'C'):
        current += 1
        if current > longest:
            longest = current
    elif current > 0:
        current = 0

print(longest)
