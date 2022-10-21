class Solution:
    def intToRoman(self, num: int) -> str:
        t3_dic = {0: '', 1: 'M', 2: 'MM', 3: 'MMM'}
        t2_dic = {0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
        t1_dic = {0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
        t0_dic = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
        digit_len = len(str(num))
        rom = ''
        while num > 0:
            digit_len -= 1
            digit = int(num/(10**digit_len))
            num = num % (10**digit_len)
            print(digit)
            if digit_len == 3:
                rom += t3_dic[digit]
            if digit_len == 2:
                rom += t2_dic[digit]
            if digit_len == 1:
                rom += t1_dic[digit]
            if digit_len == 0:
                rom += t0_dic[digit]
        return rom
s = Solution()
print(s.intToRoman(1994))