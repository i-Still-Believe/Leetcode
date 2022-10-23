from typing import List
from collections import defaultdict


class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     ans = []
    #     check = []
    #     for word in strs:
    #         found = False
    #         for group_id in range(len(check)):
    #             if sorted(word) == check[group_id]:
    #                 ans[group_id].append(word)
    #                 found = True
    #         if not found:
    #             check.append(sorted(word))
    #             ans.append([word])
    #     return ans

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for word in strs:
            cnt = [0] * 26
            for let in word:
                cnt[ord(let) - ord('a')] += 1
            ans[tuple(cnt)].append(word)
        return list(ans.values())


sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
