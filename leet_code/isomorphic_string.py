class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


if __name__ == '__main__':
    solution = Solution()
    print(solution.isIsomorphic('egg', 'add'))
    print(solution.isIsomorphic('foo', 'bar'))
    print(solution.isIsomorphic('paper', 'title'))
    print(solution.isIsomorphic('bbbaaaba', 'aaabbbba'))