import heapq
class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        heapq.heapify(nums)

        i = 0
        length = len(nums)
        while nums:
            element = heapq.heappop(nums)
            if length - i == k:
                return element
            i += 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.findKthLargest([3,2,1,5,6,4], 2))