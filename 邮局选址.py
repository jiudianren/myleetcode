

# coding =utf-8
class sol:
    '''
      若我们需要在 n 个点中选一个位置安放邮局，怎么放呢？坐标的中位数即可，奇数为中间位置，偶数任意两个中间位置之一即可。
   回到这题上来，本质是对 n 个地址进行划分，划分成 num 段，每段一个邮局，求最小的距离。
那么 dp 方程就很明显了：
   设 f [i][j] 表示 a[0--j] 安放 i 个邮局的最小距离，转移方程为:
    f[i][j]= min{f[i−1][k]+cost[k+1][j] 其中(0⩽k<n)}
    其中  cost[k+1][j]表示在  a[k+1]-a[j] 之中安放一个邮局的距离
    https://blog.csdn.net/MIC10086/article/details/112132848
    '''
    def pose(self,address: list ,num :int)->int:
        self.re = []
        for i in range(num):
            self.re.append([0xFFFFFFFF] * len(address))
        for i in range(num):
            for j in range(i+1):
                self.re[i][j] =0;

        for i in range(1, len(address)):
            self.re[0][i] = self.post_one(address[:i+1])

        for post_num in range(1,num):
            for cz_num in range(post_num+1,len(address)):
                for k in range(cz_num+1):
                    this_vale = self.re[post_num-1][k]+self.post_one(address[k+1:cz_num+1])
                    self.re[post_num][cz_num] = min(this_vale,self.re[post_num][cz_num])
        return self.re[num-1][len(address)-1]

    def post(self, address: list, num: int) -> int:
        self.re = []
        for i in range(num):
            self.re.append([0xffffff] * len(address))

        con_num = len(address)
        for i in range(con_num):
            if i <= 0:
                self.re[0][i] = 0
            else:
                self.re[0][i] = self.post_one(address[:i + 1])
        print(self.re)

        for i in range(num):
            for j in range(i + 1):
                self.re[i][j] = 0
        print(self.re)
        # 遍历村庄

        for post_index in range(1, num):
            for con_index in range(post_index + 1, con_num):
                for k in range(con_index + 1):
                    print(f"post_num:{post_index}, total_cun:{con_index}, split_k:{k}")
                    this_val = self.re[post_index - 1][k] + self.post_one(address[k + 1: con_index + 1])
                    print(f"cur_val:{this_val}={self.re[post_index - 1][k]} +{self.post_one(address[k:con_index + 1])}")
                    self.re[post_index][con_index] = min(self.re[post_index][con_index], this_val)
                    print(self.re[post_index])
        print(f"result:{self.re}")
        return self.re[num - 1][len(address) - 1]

    def post_one(self, address: list):
        if len(address) == 0:
            return 0
        pos = (len(address) + 1) // 2
        tmp = 0
        for i in address:
            tmp = tmp + abs(i - address[pos - 1])
        return tmp

    def t(self):
        num = 2
        addr = [2, 3, 7, 9, 12]
        '''
        2,3  4+6+9
        2,7 1+2+5
        3  9    1 +2+3=6

        '''

        print(self.post_one(addr))
        print(self.pose(addr, num))
        print(self.post(addr, num))


if __name__ == "__main__":
    sol().t()
