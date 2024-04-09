def canJump(nums):
    if len(nums) == 1:
        return True

    visited = [0] * len(nums)
    visited[0] = 1

    for i in range(len(nums) - 1):
        if visited[i] == 0:
            break

        for jump in range(nums[i] + 1):
            if i + jump < len(nums):
                visited[i + jump] = 1

        if visited[-1] == 1:
            return True
    
    return False


if __name__ == '__main__':
    print(canJump([2, 3, 1, 1, 4])) # True
    print(canJump([3, 2, 1, 0, 4])) # False
    print(canJump([2, 0])) # True
    print(canJump([2, 5, 0, 0])) # True
    print(canJump([1, 0, 1, 0])) # False
    print(canJump([3, 0, 8, 2, 0, 0, 1])) # True