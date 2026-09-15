class Solution:
    def trap(self, height: List[int]) -> int:
        max_ = max(height)
        sum_ = sum(height)
        total = max_ * len(height) - sum_
        i = 0
        j = len(height) - 1
        lb = 0
        rb = 0
        while i < j:
            lb = max(lb, height[i])
            total -= (max_ - lb)
            rb = max(rb, height[j])
            total -= (max_ - rb)
            if lb != max_:
                i += 1
            if rb != max_:
                j -= 1
            if rb == max_ and lb == max_:
                break
        return total