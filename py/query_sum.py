from typing import List

def countServers(grid: List[List[int]]) -> int:
        rows, cols = [0] * len(grid), [0] * len(grid[0])
        total, count = 0, 0
        
        for i, row in enumerate(grid):
            found = False
            for j, cell in enumerate(row):
                if cell == 1:
                    total += 1
                    found = True
                    cols[j] += 1
            rows[i] += found

        print(rows, cols)


solution = countServers([[0,1,0,0], 
                         [0,0,0,1]])

print(solution)