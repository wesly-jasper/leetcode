class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        t,res=[],[]
        def b(i,rem):
            if sum(t)==target:
                res.append(t[:])
                return
            for i in range(i,len(candidates)):
                if candidates[i]>rem:
                    continue
                t.append(candidates[i])
                b(i,rem-candidates[i])
                t.pop()
            return res
        return b(0,target)