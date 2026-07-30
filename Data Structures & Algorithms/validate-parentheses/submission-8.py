class Solution:
    def isValid(self, s: str) -> bool:
        '''
        most recently seen: stack
        mapping? yes -> closing to opening brackets
        when to push? opening bracket
        when to pop? when closing bracket matches most recent open bracket
        remember to check if stack is empty.
        '''
        pairs = {"}": "{", ")": "(", "]": "["}
        stack = []

        for c in s:
            if c not in pairs:
                stack.append(c)
            else:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
        return True if not stack else False