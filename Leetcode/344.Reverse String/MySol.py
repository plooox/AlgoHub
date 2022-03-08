class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        sLen = len(s)
        ret = [0 for _ in range(sLen)]
        for idx in range(sLen):
            ret[idx] = s[idx]
        
        for idx in range(sLen):
            s[idx] = ret[sLen-1 - idx]
        