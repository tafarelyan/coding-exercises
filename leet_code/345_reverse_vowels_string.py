class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        s = list(s)

        while l < r:
            if s[l] not in 'aeiouAEIOU':
                l += 1
            elif s[r] not in 'aeiouAEIOU':
                r -= 1
            elif s[l] in 'aeiouAEIOU' and s[r] in 'aeiouAEIOU':
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        return ''.join(s)

            
if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseVowels('hello'))
    print(solution.reverseVowels('leetcode'))