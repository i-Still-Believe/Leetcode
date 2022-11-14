from typing import List
from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        le = len(heights)
        left_list = [-1] * le
        right_list = [le] * le
        max_area = 0
        for base in range(le):
            left = base - 1
            while left >= 0 and heights[left] >= heights[base]:
                left = left_list[left]
            left_list[base] = left
        for base in range(le - 1, -1, -1):
            right = base + 1
            while right < le and heights[right] >= heights[base]:
                right = right_list[right]
            right_list[base] = right
        for base in range(le):
            max_area = max(max_area, (right_list[base] - left_list[base] - 1) * heights[base])
        return max_area

heights = [2,1,5,6,2,3]

sol = Solution()
print(sol.largestRectangleArea(heights))