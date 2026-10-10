class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        t,res=[],[]
        def p(s,rem):
            if sum(t)==target:
                res.append(t[:])
                return
            for i in range(s,len(candidates)):
                if i > s and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>rem:
                    break
                t.append(candidates[i])
                p(i+1,rem-candidates[i])
                t.pop()
            return res
        return p(0,target)