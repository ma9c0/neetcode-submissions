class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def subset(cur, idx):
            if idx >= len(nums):
                return [cur]
            
            next = idx + 1
            while next < len(nums) and nums[idx] == nums[next]:
                next += 1
            return subset(cur, next) + subset(cur + [nums[idx]], idx + 1)
        return subset([], 0)