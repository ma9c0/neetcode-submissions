class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                if curr < 0:
                    left += 1
                elif curr > 0:
                    right -= 1
                else:
                    sol.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return sol

