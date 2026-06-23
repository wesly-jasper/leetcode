class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        mis=[-1]*(n+1)
        for i in nums:
            mis[i]=i
        for i in range(len(mis)):
            if mis[i]==-1:
                return i
            