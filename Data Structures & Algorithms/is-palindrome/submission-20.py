class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        lower_s = s.lower()

        while l < r:
            if not lower_s[l].isalnum():
                l += 1
                continue
            if not lower_s[r].isalnum():
                r -= 1
                continue
            if lower_s[l] != lower_s[r]:
                print(s[l])
                print(s[r])
                return False
            l += 1
            r -=1
        return True
            
            
        