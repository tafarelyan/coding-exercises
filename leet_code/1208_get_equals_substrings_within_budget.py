class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = output = total = 0
        for right in range(len(s)):
            total += abs(ord(s[right]) - ord(t[right]))
            while total > maxCost:
                total -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            output = max(output, right - left + 1)

        return output

if __name__ == '__main__':
    solution = Solution()
    print(solution.equalSubstring('abcd', 'bcdf', 3))
    print(solution.equalSubstring('krrgw', 'zjxss', 19))
    print(solution.equalSubstring('pxezla', 'loewbi', 25))