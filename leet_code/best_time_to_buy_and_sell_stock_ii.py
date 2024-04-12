class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))