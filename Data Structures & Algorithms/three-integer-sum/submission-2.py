class Solution:
    def twoSum(self, numbers: List[int], target: int):
        res = []
        l, r = 0, len(numbers) - 1
        while l <= r:
            if l >= r:
                return res
            Sum = numbers[l] + numbers[r]
            if Sum == target:
                res.append([l, r])
                l += 1
                r -= 1
            elif Sum >target:
                r -= 1
            else:
                l += 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for index, num in enumerate(nums):
            sub_nums = [item for i, item in enumerate(nums) if i != index]

            tmp_list = self.twoSum(sub_nums, -1 * num) 
            if len(tmp_list) != 0: 
                res.extend([sub_nums[tmp[0]], sub_nums[tmp[1]], num] for tmp in tmp_list)
        list_of_lists = [sorted(s) for s in res]
        return [list(x) for x in set(tuple(x) for x in list_of_lists)]