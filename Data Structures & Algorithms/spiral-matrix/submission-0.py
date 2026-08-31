class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # keep track of left, right, top and bottom
        left, right, top, bottom = 0, len(matrix[0]) - 1 , 0, len(matrix) - 1

        res = []

        while left <= right and top <= bottom:
            # left to right: top += 1
            res.extend(num for num in matrix[top][left:right+1])
            top += 1
            # top to bottom: right -= 1
            res.extend(matrix[i][right] for i in range(top, bottom + 1))
            right -= 1
            if top <= bottom:
                res.extend(matrix[bottom][i] for i in range(right, left - 1, -1))
                bottom -= 1
            if left <= right:
                res.extend(matrix[i][left] for i in range(bottom, top - 1, -1))
                left += 1

        return res