class Solution:
    def summaryRanges(self, nums: list):
        if len(nums) == 0:
            return []

        result = []
        start, end = nums[0], nums[0]

        for num in nums:
            if num >= end:
                if num - end > 1:
                    if start != end:
                        result.append(f'{start}->{end}')
                    else:
                        result.append(f'{start}')

                    start = num

                end = num

        if start != end:
            result.append(f'{start}->{end}')
        else:
            result.append(f'{start}')
            
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.summaryRanges([0,1,2,4,5,7]))
    print(solution.summaryRanges([0,2,3,4,6,8,9]))