class Solution:
    def removePalindromeSub(self, s: str) -> int:
        start, end = 0, len(s)-1
        answer = 1
        while start <= end:
            if s[start] != s[end]:
                answer = 2
                break
            start += 1
            end -= 1
        return answer
