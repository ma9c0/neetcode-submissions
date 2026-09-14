class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = -1
        profit = 0
        for i, p in enumerate(prices):
            if lowest == -1 or p < lowest:
                lowest = p
            profit = max(profit, p - lowest)
        return profit