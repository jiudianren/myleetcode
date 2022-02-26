class Solution:
    def maxProfit(self, prices: list) -> int:
        stack = [prices[0],]
        max_get = 0
        for i in prices[1:]:
            if i >= stack[-1]:
                max_get= max(max_get,i - stack[-1])
            else:
                stack.append(i)
        return max_get

    def t(self):
        print(self.maxProfit([22,1,4,34,2,45]))


if __name__ == "__main__":
    Solution().t()
