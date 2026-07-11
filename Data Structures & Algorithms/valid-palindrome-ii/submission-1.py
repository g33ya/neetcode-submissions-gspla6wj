class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        - palindrome = checking left/right sides
            -> two-pointer opposite ends
        - deleting at most one character = two cases, check left/right pointer "skip"
        - skip utilizing substrings, reverse remaining string to check if palindrome
        '''

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                # two cases
                skipL, skipR = s[l+1:r+1], s[l:r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l, r = l + 1, r - 1
        return True
                    
            
