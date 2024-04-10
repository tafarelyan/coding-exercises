class Solution:
    def rotate(self, matrix: list) -> None:
        for r in range(len(matrix)):
            for c in range(r, len(matrix[r])):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp

        for row in matrix:
            row.reverse()

        print(matrix)

if __name__ == '__main__':
    solution = Solution()
    solution.rotate([
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ])