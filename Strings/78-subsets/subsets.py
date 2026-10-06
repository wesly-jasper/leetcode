class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        t=[]
        ans=[]
        def b(i):
            if i==len(nums):
                ans.append(t[:])
                return
            t.append(nums[i])
            b(i+1)
            t.pop()
            b(i+1)
            return ans
        return b(0)