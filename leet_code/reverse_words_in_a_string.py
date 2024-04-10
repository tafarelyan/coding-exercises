class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


if __name__ == '__main__':
    solution = Solution()
    print(repr(solution.reverseWords('the sky is blue')))
    print(repr(solution.reverseWords(' hello world ')))
    print(repr(solution.reverseWords('a good  example')))