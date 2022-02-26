class Solution_combine:
    def combine(self, n: int, k: int) -> list:
        temp_re =[]
        re = [temp_re,]
        nums = [i for i in range(1,n+1)]
        return self.dfs(nums, k,re)


    def dfs(self, nums:list, k:int, re:list):
        if k == 1:
            temp_re = []
            for i in nums:
                for this_re in re:
                    temp = this_re[:]
                    temp.append(i)
                    temp_re.append(temp)
            return temp_re
        else:
            if len(nums) == k:
                for this_re in re:
                    for  i in nums:
                        this_re.append(i)
                return re
            else:
                for i in nums:
                    # 当前i 被包含的情况
                    temp_re = []
                    for this_re in re:
                        temp = this_re[:]
                        temp.append(i)
                        temp_re.append(temp)
                    next_nums = nums[:]
                    next_nums.remove(i)
                    re_one = self.dfs(next_nums,k-1,temp_re)
                    re_two = self.dfs(next_nums,k,re)
                    for i in re_two:
                        re_one.append(i)
                    return re_one

    def t(self):
        print(self.combine(5,3))
