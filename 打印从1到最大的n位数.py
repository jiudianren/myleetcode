class Solution:
    def printNumbers(self, n: int) -> list:
        re =[]
        for i in range(n):
            re.append([])
        index =0
        self.dfs(n,index,re)
        for i in range(len(re)):
            re[i]= re[i][1:]
            print(re[i])
        return re[n-1]
    def dfs(self, n:int ,index:int ,re:list):
        if index == n:
            return
        for i in range(0,10):
            if index ==0:
                re[0].append(i)
            else:
                for last in re[index-1]:
                    re[index].append(i*10+last)
            print(re)
        self.dfs(n,index+1,re)

    def t(self):
        self.printNumbers(3)

Solution().t()
