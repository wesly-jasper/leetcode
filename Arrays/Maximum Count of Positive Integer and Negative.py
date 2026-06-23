class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pov=0
        neg=0
        for i in nums:
            if i>0:
                pov+=1
            elif i<0:
                neg+=1
        return max(pov,neg)