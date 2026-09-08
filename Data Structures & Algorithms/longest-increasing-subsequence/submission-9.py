class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:

        res = []
        
        for n in nums:
            if not res or n > res[-1]:
                res.append(n)
            else:
                l, r = 0, len(res) - 1
                loc = r
                while l <= r:
                    mid = (l+r) // 2
                    if res[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                
                res[loc] = n
        
        return len(res)
