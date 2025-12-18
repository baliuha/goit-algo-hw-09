# Change Calculation Algorithms Analysis

This project compares two algorithms for calculating change given a specific set of coin denominations: `[50, 25, 10, 5, 2, 1]`

### Greedy Algorithm (`find_coins_greedy`)
Iteratively selects the largest available coin.
- **Time Complexity:** In general $O(N)$, where $N$ is the number of coin denominations. But since the set of coins is fixed, the complexity is effectively $O(1)$ relative to the input `amount`. It performs a constant number of operations regardless of how large the `amount` is
- **Space Complexity:** $O(1)$, as it only stores the result dictionary

### Dynamic Programming (`find_min_coins`)
Builds a solution bottom-up to find the minimum number of coins to return.
- **Time Complexity:** The general complexity is $O(A \cdot N)$, where $A$ is the `amount` and $N$ is the number of denominations. But since coin set is fixed ($N=6$), it simplifies to $O(A)$. The execution time grows linearly with the `amount` ($A$)
- **Space Complexity:** $O(A)$, as it requires an array of size `amount` to store intermediate results (`dp` table)

### Comparison
When processing large amounts (e.g. 5000+), the difference in performance becomes more noticable:
1. **Greedy Algorithm:** Remains instantaneous. It performs simple integer division for each of the coin types.
2. **Dynamic Programming:** Performance degrades linearly with the size of the amount. To calculate change for 5000, it must calculate the optimal change for 1, 2, 3... up to 4999 first.

### Conclusion
For the coin system provided, the **Greedy Algorithm** is the better choice.
1. **Canonical Coin System:** This specific set of coins is canonical, meaning the greedy approach is guaranteed to produce the same optimal result (minimum number of coins) as the dynamic programming approach. DP is preferable to use if the coin system is non-canonical (e.g. `[4, 3, 1]`). In such a case, for an amount of 6 greedy approach will return `4 + 1 + 1` (3 coins), while DP will return `3 + 3` (2 coins)
2. **Efficiency:** The greedy algorithm is faster for large numbers and uses less memory
