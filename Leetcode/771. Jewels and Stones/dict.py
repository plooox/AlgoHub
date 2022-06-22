class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        answer = 0
        freq = {}
        
        for st in stones:
            if st not in freq:
                freq[st] = 1
            else:
                freq[st] += 1
        
        for jw in jewels:
            if jw in freq:
                answer += freq[jw]
        
        return answer