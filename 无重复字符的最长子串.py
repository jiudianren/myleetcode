
class Solution_lengthOfLongestSubstring:
    def lengthOfLongestSubstring(self, s: str) -> int:
        abc = set()
        rk =-1
        max_len =0
        for i in range(len(s)):
            if i != 0:
                abc.remove(s[i-1])
            while (rk+1!= len(s)) and (s[rk+1] not in abc):
                abc.add(s[rk + 1])
                rk = rk+1
            max_len = max(max_len,len(abc))
        return  max_len


    def t(self):
        print(self.lengthOfLongestSubstring("abcabcbb"))
        print(f"----end---")
