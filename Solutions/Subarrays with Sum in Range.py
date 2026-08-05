class Solution:
    def countSubarray(self, arr: list[int], l: int, r: int) -> int:
        
        def countAtMost(target: int) -> int:
            if target < 0:
                return 0
            
            left = 0
            current_sum = 0
            count = 0
            
            for right in range(len(arr)):
                current_sum += arr[right]
                
                while current_sum > target and left <= right:
                    current_sum -= arr[left]
                    left += 1
                
                count += (right - left + 1)
                
            return count

        return countAtMost(r) - countAtMost(l - 1)
