class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
				# 1. reverse()
                s.reverse()
				# 2. Slicing
				# s = s[::-1]  # Not run in Leetcode: Memory Complexity is not O(1)
				# s[:] = s[::1]