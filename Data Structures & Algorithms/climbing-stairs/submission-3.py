class Solution:
    def climbStairs(self, n: int) -> int:

        so_far = {1:1, 2:2}
        

        def climbing(n: int) -> int:
            if n in so_far:
                return so_far[n]

            so_far[n] = climbing(n-1) + climbing(n-2)

            return so_far[n]

        return climbing(n)