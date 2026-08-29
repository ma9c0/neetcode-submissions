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
        missing = len(t)         # TODO: a single number summarizing "how far from valid" you are

        # 2. What represents the current window, and what represents the best window found so far?
        left = 0              # TODO
        best_left, best_right = 0,0   # TODO: how will you represent "no window found yet"?

        # 3. Walk `right` forward one character at a time. For each character:
        #    - how does it affect `need` and `missing`?
        for right, ch in enumerate(s, start = 1):
            # TODO: update state for the character entering the window at `right`
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            # 4. Whenever the window is currently valid (fully covers t):
            #    try to shrink from the left as much as possible before it stops being valid.
            #    Each shrink step needs to:
            #      - check if this window beats the best one seen so far, and record it if so
            #      - undo the effect of removing s[left] from the window (update `need`/`missing`)
            #      - advance `left`
            while missing == 0:
                if best_right == 0 or right - left < best_right - best_left:
                    best_right = right
                    best_left = left
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1  # TODO: the "still valid" condition
                # TODO: compare against best, update if better
                # TODO: remove s[left] from the window's tracked state
                # TODO: advance left
                ...

        # 5. Return the answer using best_left/best_right — including the "never found one" case.
        return s[best_left:best_right]  # TODO