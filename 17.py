from typing import List
class Solution:
    def get_permutation(self, digits: str):
        if len(digits) == 0:
            pass

    def letterCombinations_simple(self, digits: str) -> List[str]:
        # letter_dict = {'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 2}
        # lettet_dict = {'2': ('a', 'b', 'c'), '3': ('d', 'e', 'f'), '4': ('g', 'h', 'i'), '5': ('j', 'k', 'l'),
        #                '6': ('m', 'n', 'o'), '7': ('p', 'q', 'r', 's'), '8': ('t', 'u', 'v'), '9': ('w', 'x', 'y', 'z')}
        # digits_len = len(digits)
        letter_dict = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs",
                '8': "tuv", '9': "wxyz"}
        sol = [''] if digits else []
        for digit in digits:
            sol = [p + q for p in sol for q in letter_dict[digit]]
        return sol

    def letterCombinations(self, digits: str) -> List[str]:
        # letter_dict = {'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 2}
        # lettet_dict = {'2': ('a', 'b', 'c'), '3': ('d', 'e', 'f'), '4': ('g', 'h', 'i'), '5': ('j', 'k', 'l'),
        #                '6': ('m', 'n', 'o'), '7': ('p', 'q', 'r', 's'), '8': ('t', 'u', 'v'), '9': ('w', 'x', 'y', 'z')}
        # digits_len = len(digits)
        letter_dict = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs",
                '8': "tuv", '9': "wxyz"}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(letter_dict[digits[0]])
            # return [p for p in letter_dict[digits[0]]]
        prev = self.letterCombinations(digits[:-1])
        additional = letter_dict[digits[-1]]
        sol = [p + q for p in prev for q in additional]
        return sol
s = Solution()
print(s.letterCombinations('23'))
