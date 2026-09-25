from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge cases: what should happen if s or t is empty, or t is longer than s?
        # TODO
        if len(t) > len(s):
            return ""

        # 1. What do you need to track about "how much of t is still unmet"?
        #    Think in terms of counts, not just set membership (t can have duplicates).
        need = Counter(t)            # TODO: a count of each character t requires
        missing = len(t)       
        left = 0              # TODO
        best_left, best_right = 0,0  
        for right, ch in enumerate(s, start = 1):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            while missing == 0:
                if best_right == 0 or right - left < best_right - best_left:
                    best_right = right
                    best_left = left
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1 

        # 5. Return the answer using best_left/best_right — including the "never found one" case.
        return s[best_left:best_right]  # TODO