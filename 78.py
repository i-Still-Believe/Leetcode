from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        le = len(nums)
        # n_bit = 1 << le
        # for i in range(2 ** le):
        #     digit = bin(i | n_bit)[3:]
        for i in range(2 ** le, 2 ** (le + 1)):
            digit = bin(i)[3:]
            ans.append([nums[x] for x in range(le) if digit[x] == '1'])
        return ans

nums = [1,2,3]
sol = Solution()
print(sol.subsets(nums))