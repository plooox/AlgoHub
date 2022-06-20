import sys

A, B = map(int, sys.stdin.readline().split())

A = int(str(A)[::-1])
B = int(str(B)[::-1])

if A > B:
    print(A)
else:
    print(B)
