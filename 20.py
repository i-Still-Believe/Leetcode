class Solution:
    def isValid(self, s: str) -> bool:
        flag = True
        stack = []
        for letter in s:
            if letter == '(' or letter == '[' or letter == '{':
                stack.append(letter)
            if letter == ')':
                if not stack:
                    flag = 0
                    break
                tmp = stack.pop()
                if tmp != '(':
                    flag = 0
                    break
            if letter == ']':
                if not stack:
                    flag = 0
                    break
                tmp = stack.pop()
                if tmp != '[':
                    flag = 0
                    break
            if letter == '}':
                if not stack:
                    flag = 0
                    break
                tmp = stack.pop()
                if tmp != '{':
                    flag = 0
                    break
        if stack:
            flag = 0
        return flag