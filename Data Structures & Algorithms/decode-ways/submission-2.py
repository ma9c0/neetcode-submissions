class Solution:
    def numDecodings(self, s: str) -> int:
        cache = dict()
        def decode(index: int):
            
            if index == len(s):
                return 1
            if index > len(s):
                return 0
            if index in cache:
                return cache[index]

            current = (decode(index+1) if s[index] != '0' else 0) + (decode(index+2) if s[index] != '0' and index < len(s) and 0 < int(s[index:index+2]) <= 26 else 0)
            cache[index] = current
            return current

            
        return decode(0)