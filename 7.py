class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            leng = len(str(x))
            res = 0
            for i in range(leng):
                tmp = x % 10
                res += tmp * 10 ** (leng-i-1)
                x = int(x / 10)
            if res<=2**31-1:
                return int(res)
            else:
                return 0
        if x<0:
            x = -x
            leng = len(str(x))
            res = 0
            for i in range(leng):
                tmp = x % 10

                res += tmp * 10 ** (leng - i - 1)
                x = int(x / 10)
            if res <= 2 ** 31:
                return -int(res)
            else:
                return 0
        if x == 0:
            return 0

x = 1534236469
sol = Solution()
ans = sol.reverse(x)
print(ans)
