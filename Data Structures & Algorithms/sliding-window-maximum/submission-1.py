class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        index_window = deque()
        res = []

        for i, num in enumerate(nums):
            while index_window and nums[index_window[-1]] <= num: 
                index_window.pop()
                
            if index_window and index_window[0] <= i - k:
                index_window.popleft()

            index_window.append(i)

            if i >= k-1 :
                res.append(nums[index_window[0]])

        return res