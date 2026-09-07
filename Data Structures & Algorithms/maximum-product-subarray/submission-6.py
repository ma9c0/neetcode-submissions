import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sub_arrays = []
        array = []
        for num in nums:
            if num != 0:
                array.append(num)
            else:
                sub_arrays.append(array)
                sub_arrays.append([0])
                array = []
        if array:
            sub_arrays.append(array)
        
        return max(self.find_max_of_subarray(array) for array in sub_arrays)
    
    def find_max_of_subarray(self, array: List[int]) -> int:
        if len(array) == 0:
            return 0
        total = math.prod(array)
        if total >= 0 or len(array) == 1:
            return total
        
        max_seen = 0
        sub_total1 = 1
        sub_total2 = total
        for i in range(len(array)):
            sub_total1 *= array[i]
            sub_total2 /= array[i]
            if array[i] < 0:
                max_seen = max(sub_total1, sub_total2, max_seen)
                break

        sub_total1 = 1
        sub_total2 = total
        for i in range(len(array) - 1, -1, -1):
            sub_total1 *= array[i]
            sub_total2 /= array[i]
            if array[i] < 0:
                max_seen = max(sub_total1, sub_total2, max_seen)
                break

        return int(max_seen)




"""
0. split array by zeros
for each of these subarrays
1. get product of everything. 
If it's positive, that is the maximum product of that subarray
If it's negative...

[2,4,-3,5]
 -120
total is negative, which means an odd number of negative numbers,
so we need to find sequence with an even number of negative numbers
candidates:
numbers from the left before first negative (0 negatives in sequence)
or same but from right side before first negative
numbers from left side after first negative (even negatives in sequence)
or same from right side
[2, 2, -1, -1, -2, 2, -2, -1, 2, 2]

"""