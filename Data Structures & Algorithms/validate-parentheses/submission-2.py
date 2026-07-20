class Solution:
    def isValid(self, s: str) -> bool:
        '''
        most recently seen: stack
        mapping? yes -> closing to opening brackets
        when to push? opening bracket
        when to pop? when closing bracket matches most recent open bracket
        remember to check if stack is empty.
        '''

        brackets = {"}": "{", "]": "[", ")": "("}
        stack = []

        for c in s:
            if c in brackets: # closing bracket
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False
            else: # open bracket
                stack.append(c)
        return True if not stack else False
