from typing import List
class Solution:
    # def canJump(self, nums: List[int]) -> bool:
    #     success = [True]
    #     i = 1
    #     le = len(nums)
    #     while i < le:
    #         current = False
    #         for t in range(1, nums[le - i - 1] + 1):
    #             current = current or success[i - t]
    #         success.append(current)
    #         i += 1
    #     return success[le - 1]


    def canJump(self, nums: List[int]) -> bool:
        le = len(nums)
        # if le == 1:
        #     return True
        i = le - 1
        last_possible = le - 1
        while i >= 0:
            if nums[i] + i >= last_possible:
                last_possible = i
            i -= 1
        return last_possible == 0


sol = Solution()
print(sol.canJump([2, 0, 0]))