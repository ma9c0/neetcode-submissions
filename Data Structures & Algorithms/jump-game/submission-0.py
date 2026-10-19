class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farest = 0

        for index, num in enumerate(nums):
            if farest < index:
                return False
            farest = max(index + num, farest)

        return len(nums) - 1 <= farest 