# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         leng = 0
#         strlen = len(s)
#         ss = '#'
#         for i1 in range(strlen):
#             ss += s[i1] + '#'
#         strlen = 2*strlen+1
#         max_list = [0]*strlen
#         for i in range(strlen):
#             j = 0
#             while i-j>=0 and i+j<strlen and ss[i-j]==ss[i+j]:
#                 j+=1
#             max_list[i] = j-1
#         max_position = max_list.index(max(max_list))
#         start = max_position-max_list[max_position]
#         end = max_position+max_list[max_position]
#         ans = ss[start:end+1]
#         ans = ans.replace('#','')
#         return ans



# Improve Manacher‘s Algorithm
# https://zhuanlan.zhihu.com/p/70532099
# https://blog.csdn.net/qq_40472064/article/details/105521142
class Solution:
    def longestPalindrome(self, s: str) -> str:

        strlen = len(s)
        ss = '#'
        for i1 in range(strlen):
            ss += s[i1] + '#'
        strlen = 2*strlen+1
        max_list = [0]*strlen

        r = 0
        c = 0

        for i in range(1, strlen):
            i_mirror = 2*c-i
            if r > i:
                max_list[i] = min(max_list[i_mirror],r-i)
            else:
                max_list[i] = 0
            while i-max_list[i]-1 >= 0 and i+max_list[i]+1 < strlen and ss[i-max_list[i]-1] == ss[i+max_list[i]+1]:
                max_list[i] += 1

            if i + max_list[i] > r:
                c = i
                r = i + max_list[i]

        max_position = max_list.index(max(max_list))
        start = max_position-max_list[max_position]
        end = max_position+max_list[max_position]
        ans = ss[start:end+1]
        ans = ans.replace('#','')
        return ans

sol = Solution()
p = sol.longestPalindrome('abcbd')
print(p)
