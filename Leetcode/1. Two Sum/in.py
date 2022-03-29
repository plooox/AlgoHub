class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for idx, n in enumerate(nums):
            sub_target = target - n
            
            if sub_target in nums[idx+1 : ]:
								#  nums.index(sub_target)은 중복되는 값 케어 x ex) [3,3]
								#  --->  nums[idx+1:].index(sub_target) + (idx + 1)
                return [nums.index(n), nums[idx+1:].index(sub_target) + (idx + 1)]