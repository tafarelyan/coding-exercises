class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        output = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            output = max(output, r-l+1)

        return output

if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring('abcabcbb'))
    # print(solution.lengthOfLongestSubstring('bbbbb'))
    # print(solution.lengthOfLongestSubstring('pwwkew'))