from typing import List
class Solution:
    # def sortColors(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     le = len(nums)
    #     cnt = [0, 0, 0]
    #     for i in range(le):
    #         if nums[i] == 0:
    #             cnt[0] += 1
    #         if nums[i] == 1:
    #             cnt[1] += 1
    #         if nums[i] == 2:
    #             cnt[2] += 1
    #     for i in range(0, cnt[0]):
    #         nums[i] = 0
    #     for i in range(cnt[0], cnt[1] + cnt[0]):
    #         nums[i] = 1
    #     for i in range(cnt[1] + cnt[0], le):
    #         nums[i] = 2

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        le = len(nums)
        red, white, blue = 0, 0, le-1
        while white <= blue:
            if nums[white] == 1:
                white += 1
            elif nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
sol = Solution()
nums = [2,0,1]
sol.sortColors(nums)
print(nums)