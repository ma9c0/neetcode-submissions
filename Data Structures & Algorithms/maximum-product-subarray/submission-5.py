class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        separated = []
        tmp = []
        cache = dict()
        while nums:
            num = nums.pop(0)
            tmp.append(num)
            if num == 0:
                if len(tmp) != 0:
                    separated.append(tmp)
                tmp = []
        if len(tmp) != 0:
            separated.append(tmp)

        answer = -math.inf
        for interval in separated:
            currentNum = interval[0]
            bestHere = interval[0]
            worstHere = interval[0]
            answer = max(bestHere, answer)
            for num in interval[1:]:
                tmp_list = [num * bestHere, num, num*worstHere]
                tmp_list.sort()
                bestHere = tmp_list[-1]
                worstHere = tmp_list[0]
                answer = max(bestHere, answer)

        return max(bestHere, answer)
