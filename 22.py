from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        temp_sol = []
        def generate(temp_sol, left=0, right=0):
            if len(temp_sol) == 2 * n:
                ans.append(''.join(temp_sol))
            else:
                if left < n:
                    temp_sol.append('(')
                    generate(temp_sol, left + 1, right)
                    temp_sol.pop()
                if right < left:
                    temp_sol.append(')')
                    generate(temp_sol, left, right + 1)
                    temp_sol.pop()
        generate(temp_sol)
        return ans



    # def generateParenthesis(self, n: int) -> List[str]:
    #     if n == 1:
    #         return ["()"]
    #     else:
    #         ans = []
    #         ans_before = self.generateParenthesis(n - 1)
    #         for element in ans_before:
    #             # if not (element[0] == '(' and element[-1:] == ')'):
    #             ans.append('(' + element + ')')
    #             ans.append(element + '()')
    #             ans.append('()' + element)
    #         return list(dict.fromkeys(ans))


sol = Solution()
print(sol.generateParenthesis(4))

# a = ["(((())))","((()))()","()((()))","((())())","(())()()","()(())()","(()(()))","()()(())","((()()))","(()())()","()(()())","(()()())","()()()()"]
# b = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
# print()
# print(set(a))
# print(set(b) - set(a))