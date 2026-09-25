class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = -1 if x <= 0 else 1
        x = abs(x)
        while x != 0:
            digit = x % 10
            x //= 10
            res = res * 10 + digit
        res *= sign
        if -2**31 > res or res > 2**31 - 1:
            return 0
        return res