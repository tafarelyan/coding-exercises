def canJump(nums):
    if len(nums) == 1:
        return 0

    visited = [0] * len(nums)
    step = 0
    visited[0] = 1

    for i in range(len(nums) - 1):
        if visited[i] == 0:
            break

        for jump in range(nums[i], 0, -1):
            if i + jump < len(nums):
                visited[i + jump] = 1

        step += 1
        if visited[-1]:
            return step

    return 0


if __name__ == '__main__':
    print(canJump([2, 3, 1, 1, 4])) # 2
    print(canJump([3, 2, 1, 0, 4])) # 0
    print(canJump([2, 0])) # 1
    print(canJump([0])) # 0
    print(canJump([2, 5, 0, 0])) # 2
    print(canJump([1, 0, 1, 0])) # 0
    print(canJump([3, 0, 8, 2, 0, 0, 1])) # 2