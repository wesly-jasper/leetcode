class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        ans=0
        for i in nums:
            if i==1:
                c+=1
            else:
                c=0
            ans=max(ans,c)
        return ans