class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        results = {}

        for index, num in enumerate(nums):
            if target - num in results:
                return [results[target-num], index]
            else:
                results[num] = index 

if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2,7,11,15], 9))
    print(solution.twoSum([3,2,4], 6))
    print(solution.twoSum([3,3], 6))