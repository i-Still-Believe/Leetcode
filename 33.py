from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        nums_len = len(nums)
        hi = nums_len - 1
        while lo != hi:
            mid = int((lo + hi) / 2)
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        anchor = lo
        lo = 0
        hi = nums_len - 1
        mid = int((lo + hi) / 2)
        real_mid = (mid + anchor) % nums_len
        while lo <= hi:
            if nums[real_mid] > target:
                hi = mid - 1
            if nums[real_mid] < target:
                lo = mid + 1
            if nums[real_mid] == target:
                return real_mid
            mid = int((lo + hi) / 2)
            real_mid = (mid + anchor) % nums_len
        return -1

sol = Solution()
nums = [4,5,6,7,0,1,2]
target = 3
print(sol.search(nums, target))