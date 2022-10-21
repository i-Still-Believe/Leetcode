class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            num = self.countAndSay(n - 1)
            current = num[0]
            cnt = 0
            ans = ''
            for i in range(len(num)):
                if num[i] == current:
                    cnt += 1
                else:
                    ans += str(cnt)
                    ans += num[i - 1]
                    cnt = 1
                    current = num[i]
            ans += str(cnt)
            ans += num[-1]
            return ans

sol = Solution()
print(sol.countAndSay(4))