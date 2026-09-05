class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        if len(s) == 1:
            return s
        for index, char in enumerate(s):
            # check left and right, if current == left or current == right, middle of left/right
            # if left == right, then middle is current

            if index != 0 and char == s[index - 1]:
                left = index - 1
                right = index
                while left >= 1 and right < len(s)-1 and s[left-1] == s[right+1]:
                    left -= 1
                    right += 1
                longest = s[left:right+1] if (right - left + 1) > len(longest) else longest
            
            if index != len(s) - 1 and index != 0 and s[index-1] == s[index+1]:
                left = index - 1
                right = index + 1
                while left >= 1 and right < len(s)-1 and s[left-1] == s[right+1]:
                    left -= 1
                    right += 1
                longest = s[left:right+1] if (right - left + 1) > len(longest) else longest

        return longest if len(longest) != 0 else s[:1]

