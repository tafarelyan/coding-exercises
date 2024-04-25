class Solution:
    def kidsWithCandies(self, candies: list, extraCandies: int) -> list:
        most_candies = max(candies)

        return [
            True if candy + extraCandies >= most_candies >= most_candies else False
            for candy in candies
        ]

if __name__ == '__main__':
    solution = Solution()
    print(solution.kidsWithCandies('Hello World'))