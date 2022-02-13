class Solution:
    def maxSubArray(self, nums: list) -> int:
        ret = -1*float("inf")
        nlen = len(nums)
        f = [-1*float("inf")]+[0]*nlen

        for i in range(nlen):
            f[i+1] = max(f[i]+nums[i], nums[i])
            #print(f"{i}-->max:{f[i+1]}")
            ret = max(ret, f[i+1])
        #print(ret)
        return ret
