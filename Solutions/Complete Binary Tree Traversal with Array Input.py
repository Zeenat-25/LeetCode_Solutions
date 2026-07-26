class Solution:
    def levelSort(self, arr):
        res = []
        n = len(arr)
        
        index = 0
        level_size = 1
        
        while index < n:
            level_nodes = arr[index : min(index + level_size, n)]
            level_nodes.sort()
            res.append(level_nodes)
            
            index += level_size
            level_size *= 2
            
        return res
