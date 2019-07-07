s = input()
ai, zi = None, 0
for i in range(len(s)):
    if ai is None and s[i] == 'A':
        ai = i

    if s[i] == 'Z':
        zi = i

print(zi - ai + 1)
