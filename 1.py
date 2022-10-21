from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i1 in range(len(nums)-1):
#             for i2 in range(i1+1,len(nums)):
#                 if nums[i1]+nums[i2]==target:
#                     return[i1,i2]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]

            if remaining in seen:
                return [i, seen[remaining]]
            seen[value] = i