from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])
        litter = {}
        start = None
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S': start = (r, c)
                elif classroom[r][c] == 'L': litter[(r, c)] = len(litter)
                
        full_mask = (1 << len(litter)) - 1
        if not full_mask: return 0

        # Queue: (r, c, mask, cur_energy, steps)
        sr, sc = start
        s_mask = (1 << litter[(sr, sc)]) if (sr, sc) in litter else 0
        
        q = deque([(sr, sc, s_mask, energy, 0)])
        visited = {(sr, sc, s_mask): energy}
        
        while q:
            r, c, mask, e, steps = q.popleft()
            if mask == full_mask: return steps
            if e == 0: continue
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    cell = classroom[nr][nc]
                    ne = energy if cell == 'R' else e - 1
                    nmask = mask | (1 << litter[(nr, nc)]) if cell == 'L' else mask
                    
                    if ne > visited.get((nr, nc, nmask), -1):
                        visited[(nr, nc, nmask)] = ne
                        q.append((nr, nc, nmask, ne, steps + 1))
                        
        return -1
