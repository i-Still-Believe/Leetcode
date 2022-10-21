class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive_dividend = dividend > 0
        positive_divisor = divisor > 0
        positive = positive_dividend is positive_divisor
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0

        while divisor <= dividend:
            current_quotient = 1
            tmp_total = divisor
            while (tmp_total << 1) < dividend:
                tmp_total <<= 1
                current_quotient <<= 1
            quotient += current_quotient
            dividend -= tmp_total

        if not positive:
            quotient = - quotient
        bound = 2 ** 31
        quotient = max(min(quotient, bound - 1), - bound)
        return quotient

    # def divide(self, dividend: int, divisor: int) -> int:
    #     positive_dividend = dividend > 0
    #     positive_divisor = divisor > 0
    #     positive = positive_dividend is positive_divisor
    #     dividend = abs(dividend)
    #     divisor = abs(divisor)
    #     quotient = 0
    #
    #     while divisor <= dividend:
    #         current_quotient = 1
    #         tmp_total = divisor
    #         while (tmp_total + tmp_total) < dividend:
    #             tmp_total += tmp_total
    #             current_quotient += current_quotient
    #         quotient += current_quotient
    #         dividend -= tmp_total
    #
    #     if not positive:
    #         quotient = - quotient
    #     bound = 2147483648
    #     quotient = max(min(quotient, bound - 1), - bound)
    #     return quotient


sol = Solution()
print(sol.divide(10, 3))
print(2 ** 31)