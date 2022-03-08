class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            # isalnum: Check is character is number or alphabet
            if char.isalnum():
                strs.append(char.lower())
            
        # Check palindrome
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False        
        return True