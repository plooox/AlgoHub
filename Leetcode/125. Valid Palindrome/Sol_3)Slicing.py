class Solution:
    def isPalindrome(self, s: str) -> bool:
		# 1. Regular Expression
        s = re.sub('[^a-z0-9]', '', s.lower())
        
		# 2. array = inverseArray
        return s == s[::-1]