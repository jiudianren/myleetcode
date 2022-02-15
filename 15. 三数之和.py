class Solution:

    def maxArea(self, height: list) -> int:
        lp = 0
        rp = len(height)-1
        ret_max = 0
        while lp < rp:
            area = min(height[lp],height[rp]) * (rp -lp)
            ret_max = max(area, ret_max)
            if height[lp]< height[rp]:
                lp =lp+1
            else :
                rp = rp -1
        return ret_max

    def threeSum(self, nums: list) -> list:
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                    # 如果指针重合，随着 b 后续的增加
                    # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                    if second == third:
                        break
                    if nums[second] + nums[third] == target:
                        ans.append([nums[first], nums[second], nums[third]])
        return ans




    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10 ** 7
        
        # 根据差值的绝对值来更新答案
        def update(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur
        print(nums)
        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                print(f"jk:{j} {k}")
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                update(s)
                if s > target:
                    k = k - 1
                else:
                    # 如果和小于 target，移动 b 对应的指针
                    j = j + 1
            return best
