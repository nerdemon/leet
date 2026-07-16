# Last updated: 7/16/2026, 3:57:27 PM
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1]*(n) for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]