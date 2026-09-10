class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            Sum = numbers[l] + numbers[r]
            if Sum >target:
                r -= 1
            else:
                l += 1
        return [l+1, r+1]