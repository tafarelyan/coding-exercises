class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        sSet = set()

        for r in range(len(s)):
            while s[r] in sSet:
                sSet.remove(s[l])
                l += 1

            sSet.add(s[r])
            longest = max(longest, r - l + 1)

        return longest

if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring('abcabcbbabcd'))