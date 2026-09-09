class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        set_nums = set(nums)
        current = 1
        looked_start = set()
        max_length = 0
        for num in set_nums:
            if num in looked_start:
                continue
            looked_start.add(num)
            while num + 1 in set_nums:
                looked_start.add(num + 1)
                current += 1
                num += 1
            max_length = max(max_length, current)
            current = 1
        return max(current, max_length) 
            