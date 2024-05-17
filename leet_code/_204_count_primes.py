class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        primes = []
        for i in range(2, n):
            is_prime = True

            for prime in primes:
                if i % prime == 0:
                    is_prime = False 
                    break
            
            if is_prime:
                primes.append(i)

        return len(primes) 

if __name__ == '__main__':
    solution = Solution()
    print(solution.countPrimes(10))
    print(solution.countPrimes(0))
    print(solution.countPrimes(1))