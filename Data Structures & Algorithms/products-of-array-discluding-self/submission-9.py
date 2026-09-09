class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        res[0] = 1
        previous_product = 1

        for index, num in enumerate(nums[:-1]):
            index += 1
            previous_product *= num
            res[index] = previous_product
        
        previous_product = 1
        nums.reverse()
        for index, num in enumerate(nums):
            res[-index-1] *= previous_product
            previous_product *= num

        return res