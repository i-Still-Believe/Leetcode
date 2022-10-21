class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            str_x = str(x)
            leng = len(str_x)
            i = 0; j = leng-1; flag = True
            while i <= j:
                if str_x[i] != str_x[j]:
                    flag = False
                    break
                i += 1; j -= 1
            return flag

sol = Solution()
p = sol.isPalindrome(123)
print(p)