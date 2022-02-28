
class Solution_generateParenthesis:

    def dfs(self,s :[], left:int, right :int , n,re):
        if len(s) ==  2*n:
            abc = "".join(s)
           # print(f"addd {abc}")
            re.append(abc)
        if left <n :
            s.append("(")
            #print(f"add ( , {s}")
            self.dfs(s,left+1,right,n ,re)
            s.pop()
        if right < left:
            #print(f"add ) , {s}")
            s.append(")")
            self.dfs(s,left, right+1, n ,re)
            s.pop()

    def generateParenthesis(self, n: int):
        '''
        括号生成
        :param n:
        :return:
        '''
        re = []
        cur_str = []
        left = 0
        right = 0
        self.dfs(cur_str,left,right,n,re)
        return re
