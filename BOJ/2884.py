import sys

H, M = map(int, sys.stdin.readline().split())

total_M = H * 60 + M
total_M -= 45

if total_M < 0:
    total_M += 60 * 24

print(divmod(total_M, 60)[0], divmod(total_M, 60)[1])
