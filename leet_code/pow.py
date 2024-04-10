class Solution:
    def myPow(self, x: float, n: int):
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = helper(x, n // 2) * helper(x, n // 2)
            return x * res if n % 2 == 1 else res
        
        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res

if __name__ == '__main__':
    solution = Solution()
    print(solution.myPow(2, 10))
    print(solution.myPow(2.1, 3))
    print(solution.myPow(2, -2))