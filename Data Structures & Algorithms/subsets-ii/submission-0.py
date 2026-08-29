class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = [[]]
        prev = idx = 0
        for i in range(len(nums)):
            idx = prev if i >= 1 and nums[i] == nums[i - 1] else 0
            prev = len(res)
            for j in range(idx, prev):
                tmp = res[j].copy()
                tmp.append(nums[i])
                res.append(tmp)
        return res