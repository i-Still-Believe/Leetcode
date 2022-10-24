from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = []
        ans.append(nums[0])
        max_value = nums[0]
        for i in range(1, len(nums)):
            if ans[i - 1] > 0:
                temp = ans[i - 1] + nums[i]
            else:
                temp = nums[i]
            if temp > max_value:
                max_value = temp
            ans.append(temp)
        return max_value
sol = Solution()
print(sol.maxSubArray([5,4,-1,7,8]))