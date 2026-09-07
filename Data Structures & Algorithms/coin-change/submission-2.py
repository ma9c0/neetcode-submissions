class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = dict()
        coins.sort()
        def get_coin(current_amount):
            if current_amount == 0:
                return 0
            if current_amount < coins[0]:
                return math.inf
            if current_amount in cache:
                return cache[current_amount]
            
            cur = min(1 + get_coin(current_amount - coin) for coin in coins if coin <= current_amount)
            cache[current_amount] = cur
            return cur

        res = get_coin(amount)
        return res if res != math.inf else -1