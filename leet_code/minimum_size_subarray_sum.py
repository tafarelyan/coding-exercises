class Solution:
    def minSubArrayLen(self, target: int, nums: list) -> int:
        shortest = len(nums)
        total = 0
        l = 0
        r = 0

        for i in range(len(nums)):
            total += nums[i]

            if total >= target:
                while total - nums[l] >= target:
                    total -= nums[l] 
                    l += 1

                shortest = min(shortest, r - l + 1)

            r += 1

        return shortest if total >= target else 0

if __name__ == '__main__':
    solution = Solution()
    print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))
    print(solution.minSubArrayLen(4, [1,4,4]))
    print(solution.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
    print(solution.minSubArrayLen(15, [5,1,3,5,10,7,4,9,2,8]))