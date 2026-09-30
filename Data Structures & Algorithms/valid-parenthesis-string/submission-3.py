class Solution:
    def checkValidString(self, s: str) -> bool:
        balance = 0
        for c in s:
            balance += 1 if c in '(*' else -1
            if balance < 0:
                return False
        balance = 0
        for c in reversed(s):
            balance += 1 if c in ')*' else -1
            if balance < 0:
                return False
        return True