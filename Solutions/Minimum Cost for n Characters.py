class Solution:
    def minCost(self, n, i, d, c):
        dp = [0] * (n + 1)

        for x in range(1, n + 1):
            # Option 1: Insert one character
            dp[x] = dp[x - 1] + i

            if x % 2 == 0:
                # Option 2: Double x/2 characters
                dp[x] = min(dp[x], dp[x // 2] + c)

            else:
                # For odd x:
                # Make x+1 characters by doubling, then delete one
                dp[x] = min(
                    dp[x],
                    dp[(x + 1) // 2] + c + d
                )

        return dp[n]
