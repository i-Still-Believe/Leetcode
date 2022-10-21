class Solution:
    def myAtoi(self, s: str) -> int:
        if s == '':
            return 0
        s = s.lstrip()
        # delete the left space, rstrip is delete the right space, strip two side
        if len(s) == 0:
            return 0
        positive = 1
        if s[0] == '-' and len(s) > 1:
            positive = -1
            s = s[1:]
            if not str(0) <= s[0] <= str(9):
                return 0
        elif s[0] == '+' and len(s) > 1:
            s = s[1:]
            if not str(0) <= s[0] <= str(9):
                return 0
        elif str(0) <= s[0] <= str(9):
            pass
        else:
            num = 0
            return num
        s = s.lstrip('0')
        if len(s) == 0 or not s[0].isdigit():
            return 0
        end = 0
        for i, c in enumerate(s):
            if c.isdigit():
                end = i+1
            else:
                break
        num = int(s[0:end])
        if positive == -1:
            if num <= 2**31:
                return -1 * num
            else:
                return -2**31
        if positive == 1:
            if num <= 2 ** 31-1:
                return num
            else:
                return 2**31-1

        return num


# improve 1
import re
class Solution:
    def myAtoi(self, s: str) -> int:
        print(*re.findall('^[\+\-]?\d+', s.lstrip()))
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)

# improve 2, same as 1
class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        str = str.lstrip()      #清除左边多余的空格
        num_re = re.compile(r'^[\+\-]?\d+')   #设置正则规则
        num = num_re.findall(str)   #查找匹配的内容
        num = int(*num) #由于返回的是个列表，解包并且转换成整数
        # * transfer list to a string
        return max(min(num,INT_MAX),INT_MIN)    #返回值

sol = Solution()
print(sol.myAtoi("+12 "))