import copy
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_Area = 0
        height_cp = heights + [0]

        for index, height in enumerate(height_cp):
            while stack and (heights[stack[-1]] >= height if index < n else True):
                h = heights[stack.pop()]
                w = index if not stack else index - stack[-1] - 1
                max_Area = max(max_Area, h * w)
            stack.append(index)
        return max_Area
