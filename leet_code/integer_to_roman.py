class Solution:
    def intToRoman(self, num: int) -> str:
        conversions = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }

        output = ""
        for n, roman in conversions.items():
            while n <= num:
                output += roman
                num -= n 
            
        return output


if __name__ == '__main__':
    solution = Solution()
    print(solution.intToRoman(3))
    print(solution.intToRoman(58))
    print(solution.intToRoman(1888))