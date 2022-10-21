class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        # protect the 1-len string
        ans = ''
        leng = len(s)
        dif_all = 2*numRows-2
        for i1 in range(numRows):
            if i1 < leng:
            # for the input like 'A', 2
                ans += s[i1]
            tmp_num = int((leng-i1)/dif_all)
            # the total number of these row, number of adding group
            dif = dif_all - i1 * 2
            # difference of every row
            for i2 in range(0, tmp_num+1):

                # if i1+dif_all*(i2+1) < leng:
                # # prevent the last letter out of index, because next is i2+1, not i2.

                if i1 != numRows-1 and i1 + dif + dif_all * i2 < leng:
                # prevent the fronter letter out of index, try the next iteration
                # because these two are not always in group, maybe odd.
                    next1 = s[i1 + dif + dif_all * i2]
                    # next position letter
                    ans += next1
                if i1 != 0 and i1+dif_all*(i2+1) < leng:
                # prevent the last letter out of index, because these two are not always in group,
                # maybe is odd, so prevent the latter out of range.
                # The fronter is protected with tmp_num, so always in range.
                    next2 = s[i1 + dif_all * (i2 + 1)]
                    # following next 2 position letter
                    ans += next2
                # +6+2,+4+4,+2+6 example.
        return ans
sol = Solution()
print(sol.convert("A", 2))
