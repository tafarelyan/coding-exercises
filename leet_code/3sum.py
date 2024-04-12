class Solution:
    def threeSum(self, nums: list) -> list:
        output = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                total = a + nums[l] + nums[r]

                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    output.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return output

if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]))
    print(solution.threeSum([0,1,1]))
    print(solution.threeSum([0,0,0]))