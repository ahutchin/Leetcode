class Solution:
    def isValid(self, s: str) -> bool:
        Stack = []

        for el in s:
            if el in "({[":
                Stack.append(el)
            else:
                if not Stack or \
                    (el == ')' and Stack[-1] != '(') or \
                    (el == ']' and Stack[-1] != '[') or \
                    (el == '}' and Stack[-1] != '{'):
                    return False
                Stack.pop()
        return not Stack
