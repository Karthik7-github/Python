def min_cost_jumps(heights):
    n = len(heights)
    if n == 0:
        return 0
    if n == 1:
        return 0
    dp = [0] * n
    dp[0] = 0
    dp[1] = abs(heights[1] - heights[0])
    for i in range(2, n):
        cost_from_one_step_back = dp[i-1] + abs(heights[i] - heights[i-1])
        cost_from_two_steps_back = dp[i-2] + abs(heights[i] - heights[i-2])
        dp[i] = min(cost_from_one_step_back, cost_from_two_steps_back)
    return dp[n-1]
heights = [20, 30, 40, 20]
result = min_cost_jumps(heights)
print(f"The minimum cost to reach the top is: {result}")