class Solution:
    
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        max_area = (r-l) * min(heights[l], heights[r])

        while l < r:
            max_area = max(max_area,(r-l) * min(heights[l], heights[r]))

            if heights[l] < heights[r]:
                l += 1
            elif heights [l] > heights[r]:
                r -= 1
            else:
                r -= 1
                l += 1
        return max_area