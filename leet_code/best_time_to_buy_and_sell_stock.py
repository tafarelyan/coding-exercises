class Solution:
    def maxProfit(self, prices):
        profit = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r

        return profit

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))