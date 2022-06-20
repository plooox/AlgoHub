import sys

nums = list(map(int, sys.stdin.readlines()))

for i in range(len(nums)):
    nums[i] = nums[i] % 42

print(len(set(nums)))
