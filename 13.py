class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        index = len(s) - 1
        t3_dic = {0: '', 1: 'M', 2: 'MM', 3: 'MMM'}
        t2_dic = {0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
        t1_dic = {0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
        t0_dic = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
        while index >= 0:
            if s[index] == 'I':
                num += 1
                index -= 1
                continue
            if s[index] == 'V':
                if index - 1 >= 0 and s[index - 1] == 'I':
                    num += 4
                    index -= 2
                else:
                    num += 5
                    index -= 1
                continue
            if s[index] == 'X':
                if index - 1 >= 0 and s[index - 1] == 'I':
                    num += 9
                    index -= 2
                else:
                    num += 10
                    index -= 1
                continue
            if s[index] == 'L':
                if index - 1 >= 0 and s[index - 1] == 'X':
                    num += 40
                    index -= 2
                else:
                    num += 50
                    index -= 1
                continue
            if s[index] == 'D':
                if index - 1 >= 0 and s[index - 1] == 'C':
                    num += 400
                    index -= 2
                else:
                    num += 500
                    index -= 1
                continue
            if s[index] == 'C':
                if index - 1 >= 0 and s[index - 1] == 'X':
                    num += 90
                    index -= 2
                else:
                    num += 100
                    index -= 1
                continue
            if s[index] == 'M':
                if index - 1 >= 0 and s[index - 1] == 'C':
                    num += 900
                    index -= 2
                else:
                    num += 1000
                    index -= 1
                continue
        return num
s = Solution()
print(s.romanToInt('MCMXCIV'))