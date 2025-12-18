import timeit
from typing import Dict, List


COINS: List[int] = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount: int) -> Dict[int, int]:
    """
    Calculates the change using a greedy algorithm.
    """
    result = {}
    for coin in COINS:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount %= coin

    return result


def find_min_coins(amount: int) -> Dict[int, int]:
    """
    Calculates the minimum number of coins needed using dynamic programming approach.
    The function guarantees the minimal number of coins for any currency system.
    """
    # initialize with infinity for all amounts except 0
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    coin_used = [0] * (amount + 1)
    for i in range(1, amount + 1):
        for coin in COINS:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    current_amount = amount

    # if the amount cannot be formed
    if dp[amount] == float('inf'):
        return {}

    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin

    return result


if __name__ == "__main__":
    small_num = 113
    print(f"-------------Test with a small number: {small_num}")
    greedy_small_num = timeit.timeit(lambda: find_coins_greedy(small_num), number=100)
    dp_small_num = timeit.timeit(lambda: find_min_coins(small_num), number=100)
    print(f"Greedy time (100 runs): {greedy_small_num:.6f}s")
    print(f"DP time (100 runs): {dp_small_num:.6f}s")

    large_num = 5248
    print(f"-------------Test with a larger number: {large_num}")
    greedy_large_num = timeit.timeit(lambda: find_coins_greedy(large_num), number=100)
    dp_large_num = timeit.timeit(lambda: find_min_coins(large_num), number=100)
    print(f"Greedy time (100 runs): {greedy_large_num:.6f}s")
    print(f"DP time (100 runs): {dp_large_num:.6f}s")
