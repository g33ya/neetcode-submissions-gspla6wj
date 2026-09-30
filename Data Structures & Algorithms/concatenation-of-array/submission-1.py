class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concat = [0] * (2 * len(nums))

        for i in range(len(nums)):
            concat[i] = nums[i]
            concat[i + len(nums)] = nums[i]

        return concat