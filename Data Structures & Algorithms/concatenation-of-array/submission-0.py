class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concat = []
        for i in range(2):
            for num in nums:
                concat.append(num)
        return concat