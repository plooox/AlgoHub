import sys

N = int(sys.stdin.readline())
answer = 0
if N % 4 == 0:
    if N % 100 != 0:
        answer = 1

if N % 400 == 0:
    answer = 1

print(answer)
