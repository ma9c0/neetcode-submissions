class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, amount = 0, len(height) - 1 , 0
        l_max, r_max = 0, -1

        while l < r and (l < len(height) and r >= 0):
            
            if height[l] < height[l_max]:
                amount += height[l_max] - height[l]
            if height[r] < height[r_max]:
                amount += height[r_max] - height[r]
            
            l_max = l  if height[l] >= height[l_max] else l_max
            r_max = r if height[r] >= height[r_max] else r_max

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return amount