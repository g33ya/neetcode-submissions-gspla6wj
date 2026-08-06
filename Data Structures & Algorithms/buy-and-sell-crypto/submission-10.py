class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        F/D: Dynamic
        Pointer jobs: right explores, left adjusts
        OE or FD: Opposite ends
        Violation condition: we want to buy low and sell high, so
        when prices[l] > prices[r], we'll want to move left to right.
        Stopping condition: for r in range(len(prices))
        '''

        max_profit = 0
        l = 0

        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)

            if prices[l] > prices[r]:
                l = r
            r += 1
        return max_profit