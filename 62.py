import numpy as np
class Solution:
    # def uniquePaths(self, m: int, n: int) -> int:
    #     table = np.ones((m, n))
    #     for ro in range(m - 2, -1,-1):
    #         for co in range(n-2,-1,-1):
    #             table[ro][co] = table[ro][co+1]+table[ro+1][co]
    #     return int(table[0][0])

    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        if m == 0 or n == 0:
            return 1
        p_m_n_n = m+n
        for i1 in range(m+n-1,n,-1):
            p_m_n_n *= i1
        p_m = m
        for i2 in range(m-1,0,-1):
            p_m*=i2
        return int(p_m_n_n / p_m)
sol = Solution()
print(sol.uniquePaths(3,7))