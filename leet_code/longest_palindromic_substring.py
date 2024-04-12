class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]

        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                start, end = i-1, i
                while start >= 0 and end < len(s):
                    if s[start] == s[end]:
                        longest = max(longest, s[start:end+1], key=lambda s: len(s))
                        start -= 1
                        end += 1
                    else:
                        break

            if i < len(s) - 1 and s[i-1] == s[i+1]:
                start, end = i-1, i+1
                while start >= 0 and end < len(s):
                    if s[start] == s[end]:
                        longest = max(longest, s[start:end+1], key=lambda s: len(s))
                        start -= 1
                        end += 1
                    else:
                        break

        return longest


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome('babad'))
    print(solution.longestPalindrome('cbbd'))
    print(solution.longestPalindrome('a'))
    print(solution.longestPalindrome('bb'))