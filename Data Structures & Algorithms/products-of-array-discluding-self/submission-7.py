class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        total_product = 1
        output = [0] * len(nums)

        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                total_product *= num

        if zero_cnt >= 2:
            return output
        elif zero_cnt == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    output[i] = total_product
                else:
                    output[i] = 0
        else:
            for i in range(len(nums)):
                output[i] = total_product // nums[i]
            
        return output