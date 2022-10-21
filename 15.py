from typing import List
class Solution:
    def twoSum(self, target: int, remaining_list: List[int]) -> List[List[int]]:
    # def twoSum(self, target: int, remaining_list: List[int]) -> List[List[int, int, int]]:
        sol = []
        i1 = 0
        # remaining_list = list(dict.fromkeys(remaining_list))
        i2 = len(remaining_list) - 1
        while i1 < i2:
            if target + remaining_list[i1] + remaining_list[i2] == 0:
                if [target, remaining_list[i1], remaining_list[i2]] not in sol:
                    sol.append([target, remaining_list[i1], remaining_list[i2]])
                i2 -= 1
            if target + remaining_list[i1] + remaining_list[i2] < 0:
                i1 += 1
            if target + remaining_list[i1] + remaining_list[i2] > 0:
                i2 -= 1
        return sol

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()
        # nums = list(dict.fromkeys(nums))
        for i1 in range(len(nums)-2):
            ans_two = self.twoSum(nums[i1], nums[i1+1:])
            if ans_two is not None:
                for item in ans_two:
                    if item not in solution:
                        solution.append(item)
        return solution

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))