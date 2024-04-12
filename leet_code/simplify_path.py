class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split('/'):
            if part:
                if part == '.':
                    continue

                if part == '..':
                    if stack: stack.pop()
                    continue

                stack.append(part)

        return '/' + '/'.join(stack)

if __name__ == '__main__':
    solution = Solution()
    print(solution.simplifyPath('/home/'))
    print(solution.simplifyPath('/../'))
    print(solution.simplifyPath('/home//foo/'))