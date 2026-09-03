class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        def get_ones(n):
            res = 0
            while n > 0:
                if n % 2 == 1:
                    res += 1
                    n -= 1
                n //= 2
            return res

        for i in range(n + 1):
            result.append(get_ones(i))

        return result