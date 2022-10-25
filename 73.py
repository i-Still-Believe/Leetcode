from typing import List
class Solution:
    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     ro = len(matrix)
    #     co = len(matrix[0])
    #     ro_zero = []
    #     co_zero = []
    #     for ro_idx in range(ro):
    #         for co_idx in range(co):
    #             if matrix[ro_idx][co_idx] == 0:
    #                ro_zero.append(ro_idx)
    #                co_zero.append(co_idx)
    #
    #     for ro_idx in range(ro):
    #         for co_idx in range(co):
    #             if ro_idx in ro_zero or co_idx in co_zero:
    #                 matrix[ro_idx][co_idx] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ro_zero = False
        co_zero = False
        ro = len(matrix)
        co = len(matrix[0])
        for ro_idx in range(ro):
            for co_idx in range(co):
                if matrix[ro_idx][co_idx] == 0:
                    if ro_idx == 0:
                        ro_zero = True
                    if co_idx == 0:
                        co_zero = True
                    matrix[ro_idx][0] = 0
                    matrix[0][co_idx] = 0

        for ro_idx in range(1, ro):
            for co_idx in range(1, co):
                if matrix[ro_idx][0] == 0 or matrix[0][co_idx] == 0:
                    matrix[ro_idx][co_idx] = 0

        if ro_zero:
            for co_idx in range(0, co):
                matrix[0][co_idx] = 0
        if co_zero:
            for ro_idx in range(0, ro):
                matrix[ro_idx][0] = 0
sol = Solution()
matrix = [[0]]
sol.setZeroes(matrix)
print(matrix)