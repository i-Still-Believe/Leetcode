class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = []
        count = 0
        for i in s:
            if i in record:
                del record[0:record.index(i)+1]
            record.append(i)

            tmp = len(record)
            if tmp > count:
                count = tmp
        return count

sol = Solution()
s = "abcabcbb"
p = sol.lengthOfLongestSubstring(s)
print(p)