class Solution:
    def canPlaceFlowers(self, flowerbed: list, n: int) -> bool:
        if n == 0:
            return True

        for i, flower in enumerate(flowerbed):
            if flower == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True

        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.canPlaceFlowers([1,0,0,0,1], n=1))
    print(solution.canPlaceFlowers([1,0,0,0,1], n=2))