class Solution:
    def merge(self, intervals: list):
        intervals.sort(key = lambda x: x[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if lastEnd >= start:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])

        return output

if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(solution.merge([[1,4],[4,5]]))
    print(solution.merge([[1,3]]))
    print(solution.merge([[1,4],[5,6]]))