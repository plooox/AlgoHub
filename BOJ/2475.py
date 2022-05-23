nums = list(map(int, input().split()))
sq_nums = [0]*len(nums)

for i in range(len(nums)):
    sq_nums[i] = nums[i]**2

print(sum(sq_nums) % 10)
