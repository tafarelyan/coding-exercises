class Solution:
    def solve(self, board: list) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            if (r, c) in visited or board[r][c] == "X" or r <= 0 or c <= 0 or r >= rows - 1 or c >= cols - 1:
                return
 
            visited.add((r, c))
            board[r][c] = "X"

            dfs(r-1, c)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r, c+1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    dfs(r, c)

        print(board)


if __name__ == '__main__':
    solution = Solution()
    solution.solve([
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ])