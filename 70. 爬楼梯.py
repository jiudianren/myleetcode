class Solution:
    def climbStairs(self, n: int) -> int:
    
        f = [0]*(n+1)
        f [0] = 1
        f[1] = 1
        for high in range(2,n+1):
            f[high] = (f[high-1]) + (f[high-2])
            #print(f"{high} {f[high]}")
        return f[n]
