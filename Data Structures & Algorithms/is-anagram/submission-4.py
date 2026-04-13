class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        | Solution: 0 |

        Finding relationship between values -> HashMap
        - Store count of chars for each string, compare maps
        """

        mapS = {}
        mapT = {}

        for letter in s:
            mapS[letter] = mapS.get(letter, 0) + 1

        for letter in t:
            mapT[letter] = mapT.get(letter, 0) + 1

        return mapS == mapT