class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        | Solution: 0 |

        Anagram -> Will need to sort/group!
        - Can use defaultdict
        - 
        """
        sortedMap = defaultdict(list)

        for s in strs:
            sorted_str = "".join(sorted(s))
            sortedMap[sorted_str].append(s)
        return list(sortedMap.values())
