def isPalindrome(l: list) -> bool:
    return l == l[::-1]
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        substrs = []
        lps = ""
        lps_len = 0
        
        for i in range(len(s)):
            sub_lps = ""
            for j in range(len(s), i, -1):
                if len(sub_lps) == 0:
                   # print(s[i:j])
                    if isPalindrome(s[i:j]) is True:
                        sub_lps = s[i:j]
            if lps_len < len(sub_lps):
                lps = sub_lps[:]
                lps_len = len(lps)
        return lps