from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        def ins(ori, new):
            ans = []
            le = len(ori[0])
            for item in ori:
                for i in range(le + 1):
                    temp = item[:]
                    temp.insert(i, new)
                    ans.append(temp)
            return ans
        len_nums = len(nums)
        ans = [[nums[0]]]
        for i in range(1, len_nums):
            ans = ins(ans, nums[i])
        return ans

sol = Solution()
print(sol.permute([1,2,3]))
