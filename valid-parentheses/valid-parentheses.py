class Solution:
    def isValid(self, s: str) -> bool:
        list = []
        for char in s:
            if char == '(':
                list.append(')')
            elif char == '{':
                list.append('}')
            elif char == '[':
                list.append(']')
            elif not list or list.pop() != char:
                return False

        return not list
        