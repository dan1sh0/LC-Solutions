class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        # 7 , 1 , 5, 3, 6, 4 
        
        l, r = 0, 1 
        total = 0
        
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r 
            else:
                total = max(total,prices[r]-prices[l])
        
            
            r+=1
        return total 
            