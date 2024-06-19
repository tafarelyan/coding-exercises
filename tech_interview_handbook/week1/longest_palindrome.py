class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_set = set()
        output = 0

        for char in s:
            if char in char_set:
                char_set.remove(char)
                output += 2
            else:
                char_set.add(char)

        if len(char_set):
            output += 1

        return output

if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome('abccccdd'))
    print(solution.longestPalindrome('a'))