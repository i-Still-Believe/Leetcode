class Solution:
    # def myPow(self, x: float, n: int) -> float:
    #     if n == 0:
    #         if x == 0.0:
    #             raise ArithmeticError
    #         else:
    #             return 1
    #     ans = 1
    #     positive = True
    #     if n < 0:
    #         n = abs(n)
    #         positive = False
    #     for i in range(n):
    #         ans *= x
    #     if not positive:
    #         return 1 / ans
    #     else:
    #         return ans
    def myPow(self, x: float, n: int) -> float:
        positive = (n > 0)
        if not positive:
            n = abs(n)
            x = 1 / x
        history = {}
        history[1] = x
        current = 1
        digit = 2
        if n == 0:
            if x == 0.0:
                raise ArithmeticError
            else:
                return 1
        while current * 2 <= n:
            x *= x
            history[digit] = x
            current *= 2
            digit *= 2

        digits = list(history.keys())
        pos = len(digits) - 1
        while current < n:
            if current + digits[pos] <= n:
                x *= history[digits[pos]]
                current += digits[pos]
            if pos > 0:
                pos -= 1
        else:
            return x


    def myPow(self, x, n):
        if abs(x) < 1e-40: return 0
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, -n)
        lower = self.myPow(x, n//2)
        if n % 2 == 0:
            return lower*lower
        if n % 2 == 1:
            return lower*lower*x




sol = Solution()
print(sol.myPow(x = 4, n = 6))
print(4 ** 6)