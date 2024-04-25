class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        hashMap = {}
        for i, num in enumerate(nums): 
            if num in hashMap:
                return [hashMap[num], i]
            else:
                hashMap[target-num] = i

if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2,7,11,15], 9))
    print(solution.twoSum([3,2,4], 6))
    print(solution.twoSum([3,3], 6))