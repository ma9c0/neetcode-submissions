class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = dict()
        def climb(at):
            if at == n:
                return 0
            if at > n:
                return math.inf
            if at in cache:
                return cache[at]
            current_cost = cost[at] + min(climb(at + 1), climb(at + 2))
            cache[at] = current_cost
            return current_cost

        return min(climb(0), climb(1))
            