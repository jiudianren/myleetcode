class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
            if len(nums)<=1:
                return []

            re =[]
            for i in nums:
                if i not in  re:
                    re.append(i)
                else:
                    re.remove(i)
            return re
