class Solution:
    def findMinArrowShots(self, points: list) -> int:
        points.sort()

        count = 1
        left, right = points[0]
        for i in range(1, len(points)):
            left_, right_ = points[i]
            if left <= left_ <= right_:
                left = max(left, left_)
                right = min(right, right_)
            else:
                count += 1
                left, right = left_, right_

        return count

if __name__ == '__main__':
    solution = Solution()
    print(solution.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
    print(solution.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))
    print(solution.findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))