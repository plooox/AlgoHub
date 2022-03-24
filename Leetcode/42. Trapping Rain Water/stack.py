class Solution:
    def trap(self, height: List[int]) -> int:
        idx_stack = []
        water_volume = 0

        for idx in range(len(height)):
            while len(idx_stack) != 0 and height[idx] > height[idx_stack[-1]]:
                top_idx = idx_stack.pop()

                if len(idx_stack) == 0:
                    break

                water_height = min(height[idx], height[idx_stack[-1]]) - height[top_idx]
                water_width = idx - idx_stack[-1] - 1

                water_volume += water_width * water_height
            idx_stack.append(idx)

        return water_volume