def max_power_dp(n: int, max_heads: int = 7) -> int:
    dp = [0] * (n + 1)
    dp[0] = 1  # нейтральный элемент по умножению
    
    for i in range(1, n + 1):
        for h in range(1, min(i, max_heads) + 1):
            dp[i] = max(dp[i], dp[i - h] * h)
    
    return dp[n]