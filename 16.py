from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = abs(nums[0] + nums[1] + nums[2] - target)
        sol = nums[0] + nums[1] + nums[2]
        # nums = nums.sort()
        # wrong
        nums.sort()
        for i1 in range(len(nums) - 2):
            i2 = i1 + 1
            i3 = len(nums) - 1
            while i2 < i3:
                diff_tmp = abs(nums[i1] + nums[i2] + nums[i3] - target)
                if diff_tmp < diff:
                    diff = diff_tmp
                    sol = nums[i1] + nums[i2] + nums[i3]
                if nums[i1] + nums[i2] + nums[i3] < target:
                    i2 += 1
                else:
                    i3 -= 1

        return sol
                    
s = Solution()
print(s.threeSumClosest([0,0,0], 1))