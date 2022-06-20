S = input()
abc = 'abcdefghijklmnopqrstuvwxyz'

for ch in abc:
    if ch in S:
        print(S.index(ch), end=' ')
    else:
        print(-1, end=' ')
