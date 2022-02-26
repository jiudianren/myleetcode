class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
            totoal_num = len(piles)
            dp = []
            for i in range(totoal_num):
                dp.append([0]*totoal_num)
            #print(dp)
            for i in range(totoal_num):
                dp[i][i] = piles[i]
            #print(dp)
            for i in range(totoal_num):
                for j in range(i+1,totoal_num):
                    one_re = piles[i] - dp[i+1][j]
                    two_re = piles[j] - dp[i][j-1]
                    dp[i][j]= max(one_re,two_re)
                    #print(f" i j {i} {j},bijiao {one_re} {two_re} ={dp[i][j]}" )
                    #print(f"re{dp[i][j]}")
            #print(dp)
            if dp[0][totoal_num-1] :
                return True
            else :
                return False
