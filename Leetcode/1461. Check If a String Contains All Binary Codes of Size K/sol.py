class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        subSet = set([])
        for i in range(k, len(s)+1):
            tmp = s[i-k:i]
            if tmp not in subSet:
                subSet.add(tmp)

        return 2**k == len(subSet)
