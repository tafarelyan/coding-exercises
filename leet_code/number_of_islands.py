class Solution:
    def numIslands(self, grid: list) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0

        def dfs(r, c):
            if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return

            visited.add((r, c))
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    count += 1

        return count

if __name__ == '__main__':
    solution = Solution()
    print(solution.numIslands([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]))