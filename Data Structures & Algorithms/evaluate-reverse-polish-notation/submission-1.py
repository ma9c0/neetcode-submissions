class Solution:
    def calculate(self, b, a, op):
        if op == '+': return a + b
        elif op == '-': return a - b
        elif op == '*': return a * b
        else: return a/b

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ['+','-','*','/']:
                stack.append(token)
            else:
                #find the two previous tokens and use token to compute and replace
                new_token = self.calculate(int(stack.pop()), int(stack.pop()), token)
                stack.append(new_token)
        return int(stack[0])