class Solution:
    def maximumSum(self, mat, k):
        n = len(mat)
        pref = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                pref[i][j] = mat[i - 1][j - 1] + pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1]
                
        max_sum = float('-inf')
        
        for i in range(k, n + 1):
            for j in range(k, n + 1):
                current_sum = pref[i][j] - pref[i - k][j] - pref[i][j - k] + pref[i - k][j - k]
                max_sum = max(max_sum, current_sum)
                
        return max_sum
