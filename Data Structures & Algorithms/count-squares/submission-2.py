class CountSquares:

    def __init__(self):
        self.points = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        self.points[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        qx, qy = point[0], point[1]
        res = 0
        for py in self.points[qx]:
            edge = abs(py - qy)
            if edge == 0:
                continue
            res += self.points[qx][py]*(self.points[qx-edge][qy] * self.points[qx-edge][py] + self.points[qx+edge][qy] * self.points[qx+edge][py])

        return res
