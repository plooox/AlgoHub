class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        boxTypes = collections.deque(boxTypes)
        boxTypes.append([0,0])
        ans = 0
        nums, units = map(int, boxTypes.popleft())
        while truckSize > 0:
            ans += units
            nums -= 1
            truckSize -= 1
            
            if nums == 0:
                nums, units = map(int, boxTypes.popleft())
        return ans