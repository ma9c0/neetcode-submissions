class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        way = dict()
        def climb(at):
            if at > n:
                return 0
            if at == n:
                return 1
            if at in way:
                return way[at]

            
            step = climb(at + 1) + climb(at + 2)
            way[at] = step
            return step

        return climb(0)