import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

mul = A * B * C
str_mul = str(mul)
count_dict = {}

for i in range(10):
    count_dict[str(i)] = 0

for ch in str_mul:
    count_dict[ch] += 1

for i in range(10):
    print(count_dict[str(i)])
