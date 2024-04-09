class Solution:
    def __init__(self) -> None:
        pass

    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start_position = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                start_position = i + 1

        return start_position


if __name__ == '__main__':
    solution = Solution()
    print(solution.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
    print(solution.canCompleteCircuit([2,3,4], [3,4,3]))
    print(solution.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]))