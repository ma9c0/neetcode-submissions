class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        current = []
        def rec(start):
            if start >= len(s):
                res.append(current.copy())

            for end in range(start, len(s)):
                sub = s[start:end+1]
                if sub == sub[::-1]:
                    current.append(sub)
                    rec(end+1)
                    current.pop()

        rec(0)
        return res