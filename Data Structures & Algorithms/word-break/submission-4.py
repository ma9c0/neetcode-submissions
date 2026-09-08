class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = dict()
        wordDict.sort(key=len, reverse=True)

        def find(state):
            if len(state) == 0:
                return True
            if state in cache:
                return cache[state]
            if not any(word == state[:len(word)] for word in wordDict):
                cache[state] = False
                return False
            state_result = any(find(state[len(word):]) for word in wordDict if word == state[:len(word)] )
            cache[state] = state_result
            return state_result

        return find(s)