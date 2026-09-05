class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def sub_rob(start, sub_num):
            rob1, rob2 = 0, 0
            for n in sub_num[start:]:
                tmp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2
            

        return max(sub_rob(0, nums[:-1]), sub_rob(1, nums))