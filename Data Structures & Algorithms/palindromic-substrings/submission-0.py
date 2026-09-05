class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0
        if len(s) == 1:
            return 1
        for index, char in enumerate(s):
            # check left and right, if current == left or current == right, middle of left/right
            # if left == right, then middle is current
            res += 1
            if index != 0 and char == s[index - 1]:
                left = index - 1
                right = index
                res += 1
                while left >= 1 and right < len(s)-1 and s[left-1] == s[right+1]:
                    left -= 1
                    right += 1
                    res += 1
            
            if index != len(s) - 1 and index != 0 and s[index-1] == s[index+1]:
                left = index - 1
                right = index + 1
                res += 1
                while left >= 1 and right < len(s)-1 and s[left-1] == s[right+1]:
                    left -= 1
                    right += 1
                    res += 1

        return res

