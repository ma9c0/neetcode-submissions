class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # for decision trees, use recursion or backtracking
        # for this problem, the key is to compute whether the state reaches target - number
        res = []

        def rec(current_sum, index, current_comb):
            if current_sum == target:
                res.append(current_comb.copy())
                return
            if index >= len(nums) or current_sum > target:
                return None 

            new_sum = current_sum + nums[index]

            current_comb.append(nums[index])
            rec(new_sum, index, current_comb)

            current_comb.pop()

            rec(current_sum, index + 1, current_comb)
            

        rec(0, 0, [])
        return res