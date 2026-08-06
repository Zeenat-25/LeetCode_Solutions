class Solution:
    def countMinOperations(self, arr):
        total_increments = 0
        max_doubles = 0
        
        for x in arr:
            if x == 0:
                continue
            
            increments_for_x = 0
            doubles_for_x = 0
            
            while x > 0:
                if x % 2 == 1:
                    increments_for_x += 1
                    x -= 1
                else:
                    doubles_for_x += 1
                    x //= 2
            
            total_increments += increments_for_x
            max_doubles = max(max_doubles, doubles_for_x)
            
        return total_increments + max_doubles
