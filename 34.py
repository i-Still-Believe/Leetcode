from typing import List
class Solution:
    # before record lo, hi
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     target_idx = -1
    #     nums_len = len(nums)
    #     lo_idx = 0
    #     hi_idx = nums_len - 1
    #     lo = 0
    #     hi = nums_len - 1
    #     find = False
    #     while lo <= hi:
    #         mid = int((lo + hi) / 2)
    #         if nums[mid] < target:
    #             lo = mid + 1
    #         if nums[mid] > target:
    #             hi = mid - 1
    #         if nums[mid] == target:
    #             target_idx = mid
    #             find = True
    #             break
    #     if find is False:
    #         return [-1, -1]
    #
    #     lo = 0
    #     hi = target_idx
    #     while lo < hi:
    #         mid = int((lo + hi) / 2)
    #         if nums[mid] < target:
    #             lo = mid + 1
    #         if nums[mid] == target:
    #             hi = mid
    #     lo_idx = hi
    #
    #     hi = nums_len - 1
    #     lo = target_idx
    #     while lo < hi:
    #         mid = int((lo + hi) / 2 + 0.5)
    #         if nums[mid] > target:
    #             hi = mid - 1
    #         if nums[mid] == target:
    #             lo = mid
    #     hi_idx = lo
    #     return [lo_idx, hi_idx]

    # after record lo hi
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     target_idx = -1
    #     nums_len = len(nums)
    #     lo_idx = 0
    #     hi_idx = nums_len - 1
    #     his_lo = 0
    #     his_hi = nums_len - 1
    #     lo = 0
    #     hi = nums_len - 1
    #     find = False
    #     while lo <= hi:
    #         mid = int((lo + hi) / 2)
    #         if nums[mid] < target:
    #             lo = mid + 1
    #             his_lo = mid
    #         if nums[mid] > target:
    #             hi = mid - 1
    #             his_hi = mid
    #         if nums[mid] == target:
    #             target_idx = mid
    #             find = True
    #             break
    #     if find is False:
    #         return [-1, -1]
    #
    #     lo = his_lo
    #     hi = target_idx
    #     while lo < hi:
    #         mid = int((lo + hi) / 2)
    #         if nums[mid] < target:
    #             lo = mid + 1
    #         if nums[mid] == target:
    #             hi = mid
    #     lo_idx = hi
    #
    #     hi = his_hi
    #     lo = target_idx
    #     while lo < hi:
    #         mid = int((lo + hi) / 2 + 0.5)
    #         if nums[mid] > target:
    #             hi = mid - 1
    #         if nums[mid] == target:
    #             lo = mid
    #     hi_idx = lo
    #     return [lo_idx, hi_idx]

    # use two binary search
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        lo_idx = 0
        hi_idx = nums_len - 1
        lo = 0
        hi = nums_len - 1
        if nums_len == 0:
            return[-1, -1]
        find = False
        while lo < hi:
            mid = int((lo + hi) / 2)
            if nums[mid] < target:
                lo = mid + 1
            if nums[mid] > target:
                hi = mid
            if nums[mid] == target:
                if find is False:
                    find = True
                hi = mid
        if nums[lo] != target and find is False:
            return [-1, -1]

        lo_idx = hi

        hi = nums_len - 1

        while lo < hi:
            mid = int((lo + hi) / 2 + 0.5)
            if nums[mid] > target:
                hi = mid - 1
            if nums[mid] == target:
                lo = mid
        hi_idx = lo
        return [lo_idx, hi_idx]



nums = [1, 2, 3]
target = 3
sol = Solution()
print(sol.searchRange(nums, target))
