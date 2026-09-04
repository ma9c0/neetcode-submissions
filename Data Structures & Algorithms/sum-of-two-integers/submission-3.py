class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            a = a & 0xFFFFFFFF
            b = b & 0xFFFFFFFF
            carry = (a&b) << 1
            a = a^b
            b = carry
        return a - (1 << 32) if a > 0x7FFFFFFF else a