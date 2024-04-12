class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        def match_pair(s: str) -> str:
            if s == '(': return ')'
            if s == '[': return ']'
            if s == '{': return '}'

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif stack:
                element = stack.pop()
                if match_pair(element) != char: 
                    return False
            else:
                return False

        return False if stack else True

if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("()"))
    print(solution.isValid("()[]{}"))
    print(solution.isValid("(]"))
    print(solution.isValid("({{{{}}}))"))