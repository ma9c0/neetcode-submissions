class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        state = deque()
        best = 0
        seen = set()

        for i in s:
            if i in seen:
                best = max(len(state), best)
                while True:
                    tmp = state.popleft()
                    seen.remove(tmp)
                    if tmp == i:
                        break

            state.append(i)
            seen.add(i)

        return max(best, len(state))