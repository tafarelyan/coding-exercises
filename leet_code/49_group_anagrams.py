from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list) -> list:
        output = defaultdict(list)

        for word in strs:
            orderedWord = ''.join(sorted(word))
            output[orderedWord].append(word)
        
        return [words for words in output.values()]

if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))