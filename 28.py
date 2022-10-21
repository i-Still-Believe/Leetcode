class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans = -1
        len_needle = len(needle)
        len_haystack = len(haystack)
        for i in range(0, len_haystack - len_needle + 1):
            if haystack[i : i + len_needle] == needle:
                ans = i
                return ans
        return ans

haystack = "leetcode"
needle = "leeto"
sol = Solution()
print(sol.strStr(haystack, needle))