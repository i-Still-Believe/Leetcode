from typing import List
class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        ro = len(board)
        co = len(board[0])

        def dfs(i, j, w):
            if w[0] != board[i][j]:
                return False
            if len(w) == 1:
                return True
            original = board[i][j]
            board[i][j] = '_'
            ans = False
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < ro and 0 <= y < co and dfs(x, y, w[1:]):
                    ans = True
                    break
            board[i][j] = original
            return ans

        for i1 in range(ro):
            for i2 in range(co):
                if dfs(i1, i2, word):
                    return True
        return False

    # def exist(self, board: List[List[str]], word: str) -> bool:
    #     direction = {0:(-1, 0),1:(0,1),2:(1,0),3:(0,-1)}
    #     # up right down left
    #     l = len(word)
    #     ro = len(board)
    #     co = len(board[0])
    #     def search(loc, length, forbidden, word_tmp):
    #         if length == 1:
    #             if board[loc[0]][loc[1]] == word[-1]:
    #                 return True
    #             else:
    #                 return False
    #         else:
    #             if board[loc[0]][loc[1]] != word[-length: -length + 1]:
    #                 return False
    #             else:
    #                 for i in range(0, forbidden):
    #                     loc_ro, loc_co = loc[0]+direction[i][0], loc[1]+direction[i][1]
    #                     if loc_ro >= 0 and loc_ro < ro and loc_co >= 0 and loc_co < co:
    #                         if board[loc_ro][loc_co] == word_tmp:
    #                             return True
    #                 for i in range(forbidden+1, 4):
    #                     loc_ro, loc_co = loc[0]+direction[i][0], loc[1]+direction[i][1]
    #                     if loc_ro >= 0 and loc_ro < ro and loc_co >= 0 and loc_co < co:
    #                         if board[loc_ro][loc_co] == word_tmp:
    #                             return True
    #                     return False
    #         else:
    #             for d in range(4):
    #                 if
    #
    #     ans = False
    #     for i1 in range(ro):
    #         for i2 in range(co):
    #             if board[i1][i2] == word[0]:
    #                 ans = True
    #
    #     if not ans:
    #         return False
board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
word = "AAAAAAAAAAAABAA"
sol = Solution()
print(sol.exist(board, word))