class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
       '''
        dp[i][0]   第i天，不持有股票的最大收益
        dp[i][1]   第i天， 持有一支股票的最大收益
        买入算复数，卖出算正数
        dp[i][0] = manx{  dp[i-1][0], dp[i-1][1] + prices[i]}
        dp[i][1] = max{ dp[i-1][1], dp[i-1][0]-prices[i]  }
        '''
        dp = []
        for i in range(len(prices)):
            dp.append([])
        #print(dp)
        dp[0].append(0)
        dp[0].append(-prices[0])
        for i in range(1,len(prices)):
            dp[i].append(max( dp[i-1][0],dp[i-1][1]+prices[i]))
            dp[i].append(max( dp[i-1][1], dp[i-1][0]-prices[i]))
        #print(dp)
        return dp[len(prices)-1][0]
