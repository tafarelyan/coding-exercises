class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matches = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        for char in s:
            if char in matches.keys():
                stack.append(char)
            else:
                if not stack or matches[stack.pop()] != char:
                    return False

        return not stack

if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid('()'))
    print(solution.isValid('()[]{}'))
    print(solution.isValid('(]'))
    print(solution.isValid('(([])){}'))