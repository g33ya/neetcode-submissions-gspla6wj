class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        - .isalnum()
        - .lower()
        - initial thought: two pointer opposite ends
        '''

        l, r = 0, len(s) - 1


        lower_s = s.lower()
        while l < r:
            if not lower_s[l].isalnum():
                l = l + 1
                continue
            if not lower_s[r].isalnum():
                r = r - 1
                continue
            
            if lower_s[l] != lower_s[r]:
                return False
            
            l, r = l + 1, r - 1
        return True



        