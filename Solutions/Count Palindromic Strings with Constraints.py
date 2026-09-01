class Solution:
    def palindromicStrings(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        total_count = 0

        for length in range(1, n + 1):
            m = (length + 1) // 2

        # If m exceeds available characters k, no valid palindrome can be formed
            if m > k:
                continue

        # Calculate P(k, m) % MOD
            permutations = 1
            for i in range(m):
                permutations = (permutations * (k - i)) % MOD

            total_count = (total_count + permutations) % MOD

        return total_count
