S = ''.join(reversed(input().strip()))

words = [''.join(reversed(w)) for w in ['dream', 'dreamer', 'erase', 'eraser']]


def contains(s):
    for w in words:
        if s.startswith(w):
            return len(w)
    return -1


def check(S):
    i = 0
    while i <= len(S) - 1:
        res = contains(S[i:])
        if res < 0:
            return False
        else:
            i += res

    return True


if check(S):
    print('YES')
else:
    print('NO')
