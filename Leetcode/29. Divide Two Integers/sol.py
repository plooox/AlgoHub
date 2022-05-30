class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a, b, answer = abs(dividend), abs(divisor), 0

        if (dividend == -2147483648) and (divisor == -1):
            return 2147483647

        for x in range(32)[::-1]:
            if (a >> x) >= b:
                answer += 1 << x
                a -= b << x
        if (dividend > 0) == (divisor > 0):
            return answer
        else:
            return -answer
