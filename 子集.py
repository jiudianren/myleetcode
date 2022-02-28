class Solution_subsets:

    def subsets(self, nums: list) -> list:
        '''
        子集
        :param nums:
        :return:
        '''
        self.re = []
        cur_re = []
        self.dfs(nums,0, cur_re)
        print(self.re)
        return self.re
    def dfs(self, nums:list, index:int , cur_re:list):
        if index == len(nums):
            print(f"{index}, {len(nums)}")
            self.re.append(cur_re[:])
            return
        self.dfs(nums, index+1, cur_re)
        cur_re.append(nums[index])
        self.dfs(nums,index+1,cur_re)
        cur_re.pop()
    def  t(self):
        self.subsets([1,3,4,12,41])
