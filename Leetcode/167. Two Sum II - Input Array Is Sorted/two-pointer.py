class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        f, l = 0, len(numbers)-1

        while f < l:
            if numbers[f] + numbers[l] == target:
                return [f+1, l+1]

            if numbers[f] + numbers[l] > target:
                l -= 1
            else:
                f += 1
