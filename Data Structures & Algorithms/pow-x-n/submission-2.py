class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            if x == 0:
                return 0
            
            res = helper(x, n // 2)
            
            res = res * res
            
            if n % 2 != 0:
                return x * res
            else:
                return res
        
        ans = helper(x, abs(n))
        
        if n >= 0:
            return ans
        else:
            return 1 / ans