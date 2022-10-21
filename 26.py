from typing import List
class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     current = nums[0]
    #
    #     i = 1
    #     num_len = len(nums)
    #     while i < num_len:
    #         if nums[i] == current:
    #             del nums[i]
    #             i -= 1
    #             num_len -= 1
    #         if nums[i] > current:
    #             current = nums[i]
    #         i += 1
    #     length = len(nums)
    #     return length
    def removeDuplicates(self, nums: List[int]) -> int:
        current_pos = 1
        for i in range(0, len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[current_pos] = nums[i + 1]
                current_pos += 1
        return current_pos

nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
print(sol.removeDuplicates(nums))