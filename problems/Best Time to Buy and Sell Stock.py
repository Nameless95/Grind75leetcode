class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices

        minprice = max(prices)
 
        maxprofits = 0

        for x in prices:

            if x < minprice:
        
                minprice = x
         
  
          
            if x - minprice  > maxprofits:
                maxprofits = x - minprice

        return maxprofits