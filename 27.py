from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        current_pos = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[current_pos] = nums[i]
                current_pos += 1
        return current_pos


nums = [0,1,2,2,3,0,4,2]
val = 2
sol = Solution()
print(sol.removeElement(nums, val))