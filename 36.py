from typing import List
class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     ans = True
    #     for i1 in range(9):
    #         ro = board[i1]
    #         if len(set(ro)) - 1!= len([x for x in ro if x!='.']):
    #             ans = False
    #             return ans
    #         co = []
    #         for i2 in range(0, 9):
    #             co.append(board[i2][i1])
    #         if len(set(co)) - 1 != len([x for x in co if x != '.']):
    #             ans = False
    #             return ans
    #
    #     start = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    #     start_pos = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    #     pos = 0
    #     while pos < 9:
    #         square = []
    #         count = 0
    #         while count < 9:
    #             cor = [sum(tup) for tup in zip(start_pos[pos], start[count])]
    #             square.append(board[cor[0]][cor[1]])
    #             count += 1
    #         pos += 1
    #         if len(set(square)) - 1 != len([x for x in square if x != '.']):
    #             ans = False
    #             return ans
    #     return ans

    # def isValidSudoku(self, board):
    #     seen = sum(([(c, i), (j, c), (int(i / 3), int(j / 3), c)]
    #                 for i in range(9) for j in range(9)
    #                 for c in [board[i][j]] if c != '.'), [])
    #     return len(seen) == len(set(seen))

    def isValidSudoku(self, board):
        seen = []
        for i1 in range(9):
            for i2 in range(9):
                if board[i1][i2] != '.':
                    seen.append((i1, board[i1][i2]))
                    seen.append((board[i1][i2], i2))
                    seen.append((int(i1 / 3), int(i2 / 3), board[i1][i2]))
        if len(set(seen)) != len(seen):
            return False
        else:
            return True

sol = Solution()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(sol.isValidSudoku(board))