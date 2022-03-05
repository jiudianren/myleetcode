
class Solution_longestPalindrome:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <2:
            return s
        re_str =""
        max_len =0
        dp =[]
        for i in range(len(s)):
            dp.append([False]*len(s))
        for i in range(len(s)):
            maxlen =1
            re_str = s[i]
            dp[i][i] = True
        #对长度遍历
        for i in range(2,len(s)+1):
            #对序列开始遍历
            for start_index in range(len(s)-i+1):
                right_index = start_index + i-1
                print(f"{i},{start_index},{right_index}")
                if s[start_index] != s[right_index]:
                    dp[start_index][right_index] = False
                else:
                    if right_index - start_index <3:
                        dp[start_index][right_index] = True
                    else:
                        dp[start_index][right_index] = dp[start_index+1][right_index-1]
                if dp[start_index][right_index] :
                    if right_index - start_index +1 >maxlen:
                        maxlen = right_index - start_index +1
                        re_str = s[start_index:right_index+1]
        return re_str
    def t(self):
        print(self.longestPalindrome(f"ac"))
        print(self.longestPalindrome(f"abdefecd"))
