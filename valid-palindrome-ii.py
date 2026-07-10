class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        """
        - use two pointer (l/r)
        - can delete at most one character -> "skip" char with substrings, check reversal for
            valid palindrome
        - important: will need to check "skip" of both l/r elements (2 checks!)
        """

        l, r = 0, len(s) - 1

        while l < r:
            if (s[l] != s[r]):
                skipL, skipR = s[l+1:r + 1], s[l:r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l, r = l + 1, r -1
        return True

        
