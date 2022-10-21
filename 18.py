from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        sols = []
        # i1 = 0
        # i2 = len(nums) - 1
        # flag = 2
        # # 0 for i1, 1 for i2, 2 for both finish
        # while i2 - i1 >= 3:
        for i1 in range(0, len(nums) - 3):
            for i2 in range(i1 + 3, len(nums)):
                i3 = i1 + 1
                i4 = i2 - 1
                while i3 < i4:
                    value = nums[i1] + nums[i2] + nums[i3] + nums[i4]
                    if value < target:
                        i3 += 1
                    if value > target:
                        i4 -= 1
                    if value == target:
                        if [nums[i1], nums[i3], nums[i4], nums[i2]] not in sols:
                            sols.append([nums[i1], nums[i3], nums[i4], nums[i2]])
                        i3 += 1
                        i4 -= 1
                # if flag == 2:
                #     i1 += 1
                #     flag = 0
                #     continue
                # if flag == 0:
                #     i1 -= 1
                #     i2 -= 1
                #     flag = 1
                #     continue
                # if flag == 1:
                #     i1 += 1
                #     flag = 2
                #     continue
        return sols

s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))

