d = [int(input()) for _ in range(5)]
k = int(input())

if d[4] - d[0] <= k:
    print('Yay!')
else:
    print(':(')
