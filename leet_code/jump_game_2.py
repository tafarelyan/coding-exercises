def canJump(nums):
    step = 0
    l = r = 0

    while r < len(nums) - 1:
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(farthest, i + nums[i])
        l = r + 1
        r = farthest

        if l > r:
            return -1

        step += 1

    return step
        

if __name__ == '__main__':
    print(canJump([2, 3, 1, 1, 4])) # 2
    print(canJump([3, 2, 1, 0, 4])) # -1
    print(canJump([2, 0])) # 1
    print(canJump([0])) # 0
    print(canJump([2, 5, 0, 0])) # 2
    print(canJump([1, 0, 1, 0])) # -1
    print(canJump([3, 0, 8, 2, 0, 0, 1])) # 2