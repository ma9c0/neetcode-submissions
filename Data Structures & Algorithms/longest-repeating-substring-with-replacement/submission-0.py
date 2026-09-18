class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = k + 1
        l = 0
        seen = Counter()

        for r in range(len(s)):
            seen[s[r]] += 1
            need = (r - l + 1) - max(seen.values())
            if need > k:
                seen[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest