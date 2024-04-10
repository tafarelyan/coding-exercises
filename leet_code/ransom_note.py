from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = defaultdict(int)

        for char in magazine:
            magazine_counter[char] += 1

        for char in ransomNote:
            if char in magazine_counter and magazine_counter[char] > 0: 
                magazine_counter[char] -= 1
            else:
                return False

        return True

if __name__   == "__main__":
    solution = Solution()
    print(solution.canConstruct('a', 'b'))
    print(solution.canConstruct('aa', 'ab'))
    print(solution.canConstruct('aa', 'aab'))