class Solution:
    def maxArea(self, height: list) -> int:
        lp = 0
        rp = len(height)-1
        ret_max = 0
        while lp < rp:
            area = min(height[lp],height[rp]) * (rp -lp)
            print(area)
            ret_max = max(area, ret_max)
            if height[lp]< height[rp]:
                lp =lp+1
            else :
                rp = rp -1
        return ret_max
