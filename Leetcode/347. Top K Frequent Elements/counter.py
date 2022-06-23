class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        heap = []
        
        for f in freq:
            heapq.heappush(heap, (-freq[f], f))
        
        answer = []
        
        for _ in range(k):
            answer.append(heapq.heappop(heap)[1])
        
        return answer