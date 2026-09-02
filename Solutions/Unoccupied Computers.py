class Solution:
    def solve(self, n, s):
        allocated = set()
        turned_away = set()
        
        for char in s:
            if char in allocated:
                # Customer is leaving after using a computer
                allocated.remove(char)
            elif char in turned_away:
                # Customer is leaving after being turned away (no effect on computers)
                continue
            else:
                # Customer is arriving
                if len(allocated) < n:
                    allocated.add(char)
                else:
                    turned_away.add(char)
                    
        return len(turned_away)
