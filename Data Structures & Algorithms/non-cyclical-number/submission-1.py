class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = []

        while sum([i** 2 for i in [int(d) for d in str(n)]]) not in seen:
            if sum([i** 2 for i in [int(d) for d in str(n)]]) == 1:
                return True
            seen.append(sum([i** 2 for i in [int(d) for d in str(n)]]))
            n = sum([i** 2 for i in [int(d) for d in str(n)]])

        return False
