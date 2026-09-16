class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        N = n + k - 1
        R = 2 * k
        
        if R > N:
            return 0
        
        # Calculate C(N, R) % MOD
        # C(N, R) = N! / (R! * (N - R)!)
        R = min(R, N - R)
        
        numerator = 1
        denominator = 1
        
        for i in range(1, R + 1):
            numerator = (numerator * (N - i + 1)) % MOD
            denominator = (denominator * i) % MOD
            
        # Fermat's Little Theorem for modular inverse: denominator^(MOD-2) % MOD
        return (numerator * pow(denominator, MOD - 2, MOD)) % MOD
