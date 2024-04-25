class Solution:
    def numOfSubarrays(self, arr: list, k: int, threshold: int) -> int:
        if k > len(arr): return 0

        total = sum(arr[:k-1])
        output = 0

        for i in range(len(arr)-k+1):
            total += arr[i + k - 1]
            if total / k >= threshold:
                output += 1

            total -= arr[i]

        return output
        

if __name__ == '__main__':
    solution = Solution()
    print(solution.numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))
    print(solution.numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5))