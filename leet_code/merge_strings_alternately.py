class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        output = ''
        while i < len(word1) and i < len(word2):
            output += word1[i] + word2[i]
            i += 1

        output += word1[i:] + word2[i:]

        return output

if __name__ == '__main__':
    solution = Solution()
    print(solution.mergeAlternately('abc', 'pqr'))