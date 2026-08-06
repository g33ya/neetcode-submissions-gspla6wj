class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        OE or SD: Opposite Ends
        Left moves: while not alnum
        Right moves: while not alnum
        Stopping condition: !(l < r)
        '''

        # Case in-sensitive
        lower_s = s.lower()
        l, r = 0, len(lower_s) - 1

        while l < r:
            while l < r and not lower_s[l].isalnum():
                l += 1
            while l < r and not lower_s[r].isalnum():
                r -= 1

            if lower_s[l] != lower_s[r]:
                return False
            l += 1
            r -= 1
        return True

