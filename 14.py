from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ''
        min_len = len(strs[0])
        for item in strs:
            if len(item) < min_len:
                min_len = len(item)
        for i in range(min_len):
            cha = strs[0][i]
            flag = 1
            for item_idx in range(len(strs)):
                if strs[item_idx][i] != cha:
                    flag = 0
                    break
            if flag:
                common += strs[0][i]
            else:
                break

        return common


s = Solution()
print(s.longestCommonPrefix(["cir","car"]))