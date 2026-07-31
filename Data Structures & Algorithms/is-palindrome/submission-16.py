class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        reading forward/backward = two-pointer opposite ends
        ignores all non-alphanumeric -> isalnum()

        movement condition: s[l] == s[r] OR not s[l].isalnum()
        stopping condition: while l < r OR s[l] != s[r]
        '''

        l, r = 0, len(s) - 1
        lower_s = s.lower()

        while l < r:
            while l < r and not lower_s[l].isalnum():
                l += 1
            while l < r and not lower_s[r].isalnum():
                r -= 1

            if lower_s[l] != lower_s[r]:
                return False
            
            l, r = l + 1, r - 1
        return True
