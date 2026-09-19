class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)

        res = []

        def rec(current_sum, current_comb, index):
            if current_sum == target:
                res.append(current_comb.copy())
                return 
            if index >= len(candidates) or current_sum > target:
                return
            
            current_comb.append(candidates[index])
            rec(current_sum + candidates[index], current_comb, index + 1)

            current_comb.pop()
            skip_cand = index 
            while skip_cand < len(candidates) and candidates[skip_cand] == candidates[index]:
                skip_cand += 1
            rec(current_sum, current_comb, skip_cand)

        rec(0,[], 0)

        return res