class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []

        for passenger, start, end in trips:
            events.append((start, passenger))
            events.append((end, -passenger))

        events.sort(key=lambda event: (event[0], event[1]))

        onboard = 0
        for _, change in events:
            onboard += change
            if onboard > capacity:
                return False

        return True 