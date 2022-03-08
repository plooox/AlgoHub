class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_alphabet = []
        for ch in s:
            if ch.isalnum() == True:
                str_alphabet.append(ch.lower())
        
        idx = 0
        strlen = len(str_alphabet)
        while idx < strlen:
            if str_alphabet[idx] != str_alphabet[strlen-idx-1]:
                return False
            idx += 1
        
        return True