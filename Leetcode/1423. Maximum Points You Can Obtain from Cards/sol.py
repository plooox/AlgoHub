class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        leng = len(cardPoints)
        curmax = rightmost = sum([cardPoints[leng - 1 - i] for i in range(k)])

        print(rightmost)
        for i in range(k):
            rightmost = rightmost - cardPoints[leng - k + i] + cardPoints[i]
            if rightmost > curmax:
                curmax = rightmost

        return curmax
