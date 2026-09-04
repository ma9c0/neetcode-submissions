class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = dict()
        def take(house):
            if house > len(nums) - 1:
                return 0
            if house in cache:
                return cache[house]
            cur_max = max(nums[house] + take(house + 2), take(house + 1))
            cache[house] = cur_max
            return cur_max

        return take(0)