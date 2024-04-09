def canJump(nums):
    goal = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return True if goal == 0 else False


if __name__ == '__main__':
    print(canJump([2, 3, 1, 1, 4])) # True
    print(canJump([3, 2, 1, 0, 4])) # False
    print(canJump([2, 0])) # True
    print(canJump([2, 5, 0, 0])) # True
    print(canJump([1, 0, 1, 0])) # False
    print(canJump([3, 0, 8, 2, 0, 0, 1])) # True