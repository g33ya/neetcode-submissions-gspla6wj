class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        fixed or dynamic? dynamic
        - rule: move pointers while rules are violated
        here, we want to buy low and sell high
        - find lowest price and highest price following
        - if right is < left, move right until it's at left
        '''
        l, r = 0, 1
        max_profit = 0

    

        while r < len(prices):
            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)

            if prices[r] < prices[l]:
                r = l
                l += 1
            r += 1
            
        return max_profit