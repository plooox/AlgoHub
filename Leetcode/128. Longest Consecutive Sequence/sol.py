import heapq


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                cur = num
                cur_len = 1

                while cur + 1 in nums:
                    cur += 1
                    cur_len += 1

                answer = max(answer, cur_len)

        return answer
