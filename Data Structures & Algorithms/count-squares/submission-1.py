class CountSquares:

    def __init__(self):
        self.points = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        self.points[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        # points are stored for each x value, there is a counter of y coordinate
        # iterate through those points with the same x value as query x, calculate diff in y
        # and check of other two points
        qx, qy = point[0], point[1]
        res = 0
        for py in self.points[qx]:
            edge = abs(py - qy)
            if edge == 0:
                continue
            res += self.points[qx][py]*(self.points[qx-edge][qy] * self.points[qx-edge][py] + self.points[qx+edge][qy] * self.points[qx+edge][py])

        return res
