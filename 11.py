from typing import List



# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         leng = len(height)
#         max_area_all = 0
#         for i1 in range(leng-1):
#             # min_height = height[i1]
#             max_area = 0
#             for i2 in range(i1+1, leng):
#                 # if height[i2] < min_height:
#                 #     min_height = height[i2]
#                 area = (i2 - i1) * min(height[i1], height[i2])
#                 if area > max_area:
#                     max_area = area
#             if max_area > max_area_all:
#                 max_area_all = max_area
#         return max_area_all


class Solution:
    def maxArea(self, height: List[int]) -> int:
        leng = len(height)
        max_area_all = 0
        i1 = 0
        i2 = leng-1
        while i1 < i2:
            area = (i2 - i1) * min(height[i1], height[i2])
            if area > max_area_all:
                max_area_all = area
            if height[i1] < height[i2]:
                i1 += 1
            else:
                i2 -= 1
        return max_area_all


s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))