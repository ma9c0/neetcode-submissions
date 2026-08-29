class Solution:
    
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        left = ["{", "(", "["]
        right = ["}", ")", "]"]
        stack = []
        for i in s:
            if i in left:
                stack.append(i)
            else:
                if len(stack) <= 0:
                    return False
                if i == right[left.index(stack[-1])]:
                    stack.pop()
                else:
                    return False
        return True if len(stack) ==0 else False
        