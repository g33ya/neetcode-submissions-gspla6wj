class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Push: Opening brackets
        Pop: Closing brackets
        Mapping?: Closing to open
        Violation: stack[-1] not the corresponding bracket
        Empty check: in final return (return True if not stack)
        '''

        stack = []
        bracket_pairs = {"}": "{", "]": "[", ")": "("}

        for c in s:
            if c not in bracket_pairs:
                stack.append(c)
            else:
                if not stack or stack[-1] != bracket_pairs[c]:
                    return False
                stack.pop()
        return True if not stack else False 