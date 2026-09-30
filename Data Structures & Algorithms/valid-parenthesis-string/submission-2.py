class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0  # Minimum possible unmatched '('
        max_open = 0  # Maximum possible unmatched '('

        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1

            elif char == ')':
                min_open -= 1
                max_open -= 1

            else:  # '*'
                # '*' is ')' for the minimum, '(' for the maximum
                min_open -= 1
                max_open += 1

            # Even the most favorable interpretation has too many ')'
            if max_open < 0:
                return False

            # The minimum cannot be negative; '*' can act as empty
            min_open = max(0, min_open)

        # A valid interpretation must be able to end with zero unmatched '('
        return min_open == 0
