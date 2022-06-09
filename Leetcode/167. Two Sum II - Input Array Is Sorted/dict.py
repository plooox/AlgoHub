class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        dic = {}

        for idx, num in enumerate(numbers):

            if target - num in dic:
                return [dic[target - num] + 1, idx + 1]
            dic[num] = idx
