class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_ptr(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]
        
        # Exception Handling for performance
        if len(s) < 2 or s == s[::-1]:
            return s
        
        res = ''
        for i in range(len(s) - 1):
            res = max(res,  
                        expand_ptr(i, i+1),  # win1
                        expand_ptr(i, i+2),  # win2
                        key = len
                     )
        
        return res