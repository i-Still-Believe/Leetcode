from typing import List
class Solution:
    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     ans = []
    #     global i
    #     # intervals = sorted(intervals, key=lambda t: t[0])
    #     intervals.sort(key=lambda t: t[0])
    #     le = len(intervals)
    #     pos = 0
    #     while pos < le:
    #         right = intervals[pos][1]
    #         for i in range(pos + 1, le):
    #             if intervals[pos][1] >= intervals[i][0]:
    #                 if intervals[i][1] > right:
    #                     right = intervals[i][1]
    #                 if i == le - 1:
    #                     i += 1
    #             else:
    #                 break
    #         ans.append([intervals[pos][0], right])
    #         if i == pos:
    #             i += 1
    #         pos = i
    #
    #     return ans
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort(key=lambda t: t[0])
        le = len(intervals)
        for interval in intervals:
            if not ans or interval[0] > ans[-1][1]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans

sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))