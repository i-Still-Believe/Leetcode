from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ro = len(matrix)
        co = len(matrix[0])
        path = ro * co
        pos = 0
        ro_pos = 0
        co_pos = 0
        ans = []
        direction = (0, 1)
        change = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
        pass_history = []
        while pos < path:
            pos += 1
            ans.append(matrix[ro_pos][co_pos])
            pass_history.append((ro_pos, co_pos))
            new_ro_pos = ro_pos + direction[0]
            new_co_pos = co_pos + direction[1]
            if new_ro_pos >= ro or new_co_pos >= co or new_ro_pos < 0 or new_co_pos < 0 or (new_ro_pos, new_co_pos) in pass_history:
                direction = change[direction]
            ro_pos = ro_pos + direction[0]
            co_pos = co_pos + direction[1]
        return ans

sol = Solution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))