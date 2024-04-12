class Solution:
    def maxArea(self, height: list) -> int:
        l, r = 0, len(height)-1
        area = 0

        while l < r:
            area = max(area, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return area

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))