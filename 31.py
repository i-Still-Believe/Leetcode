from typing import List
import copy
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = False
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                idx = i - 1
                flag = True
                for j in range(i, len(nums)):
                    if nums[j] <= nums[i - 1]:
                        idx = j - 1
                        break
                    else:
                        idx = j

                nums[i - 1], nums[idx] = nums[idx], nums[i - 1]
                nums[i:] = list(reversed(nums[i:]))
                # here is slower than just manually in-place swap
                return
        if flag is False:
            nums.reverse()
            return
sol = Solution()
nums = [3, 2, 1]
print(sol.nextPermutation(nums))