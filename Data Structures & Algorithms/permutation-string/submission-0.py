class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set_s1 = dict(Counter(list(s1)))
        start_index = 0

        while start_index + len(s1) <= len(s2):
            end_index = start_index + len(s1)
            current_window = dict(Counter(list(s2)[start_index:end_index]))
            if current_window == set_s1:
                return True
            else: 
                print(start_index, end_index)
                print(current_window, set_s1)
                start_index += 1

        return False
        