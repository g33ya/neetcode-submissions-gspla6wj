# Relationship between i and j
# What is the minimum amount of information I can store to achieve one pass?

# 3 + 4 = 7  -> 7 - 3 = 4
# 3 + ? = target, target - i = ___ (j)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}

        for i in range(len(nums)):
            if (target - nums[i]) in sums:
                return [sums[target-nums[i]], i]
            else:
                sums[nums[i]] = i
        
        