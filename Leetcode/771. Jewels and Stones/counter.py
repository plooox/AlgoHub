class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        answer = 0
        counter = collections.Counter(stones)
        
        for jw in jewels:
            if jw in counter:
                answer += counter[jw]
        
        return answer