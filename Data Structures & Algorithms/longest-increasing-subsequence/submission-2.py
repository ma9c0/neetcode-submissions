class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = dict()
        def keep(index, start):
            if index >= len(nums) or start >= len(nums):
                return 0
            if (index, start) in cache:
                return cache[(index, start)]
            
            tmp_res = max(
                keep(index + 1, start), 
                (keep(index + 1, index) + 1) if nums[index] > nums[start] or start == -1 else -1
            )
            cache[(index, start)] = tmp_res
            return tmp_res

        return keep(0,-1)