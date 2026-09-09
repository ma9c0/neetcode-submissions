class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                tmp = stack.pop()
                print(tmp, index)
                res[tmp] = index - tmp
            stack.append(index)

        return res