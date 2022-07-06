class Solution:
    def fib(self, n: int) -> int:
        memo = [0 for _ in range(31)]
        memo[1] = 1

        if n > 1:
            for i in range(2, n+1):
                memo[i] = memo[i-1] + memo[i-2]

        return memo[n]
