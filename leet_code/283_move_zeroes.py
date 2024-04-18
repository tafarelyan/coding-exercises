class Solution:
    def moveZeroes(self, nums: list) -> None:
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1


if __name__ == '__main__':
    solution = Solution()
    solution.moveZeroes([0,0,1,3,12])
    solution.moveZeroes([0,1,0,3,12])
    solution.moveZeroes([1,0])