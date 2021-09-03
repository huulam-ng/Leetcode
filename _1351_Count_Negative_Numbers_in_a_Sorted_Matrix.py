class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(0,len(grid)):
            for j in grid[i]:
                if j < 0:
                    count += 1
        return count