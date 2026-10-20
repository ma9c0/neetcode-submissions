class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(i, cur):
            if i == len(s):
                res.append(cur.copy())
                return
            
            for j in range(i, len(s)):
                if self.is_pal(s, i, j):
                    cur.append(s[i : j + 1])
                    backtrack(j + 1, cur)
                    cur.pop()
        
        backtrack(0, [])
        return res
        
    def is_pal(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True