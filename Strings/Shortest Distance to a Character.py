class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n=len(s)
        dp=[n]*n
        prev=-n
        for i in range(n):
            if s[i]==c:
                prev=i
            dp[i]=i-prev
        prev=2*n
        for i in range(n-1,-1,-1):
            if s[i]==c:
                prev=i
            dp[i]=min(dp[i],prev-i)
        return dp