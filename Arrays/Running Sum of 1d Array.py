class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        c=0
        arr=[]
        for i in nums:
            c+=i
            arr.append(c)
        return arr