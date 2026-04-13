class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        | Solution: 0 |

        Relationship between values -> HashMap
        - Store difference of (target - current num) with index value
        - Check if current num is in map -> return
        """

        sums = {}

        for i in range(0, len(nums)):
            if nums[i] in sums:
                return [sums.get(nums[i], 0), i]
            sums[target - nums[i]] = i
        

