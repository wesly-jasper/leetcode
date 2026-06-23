class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        a=[]
        su=[]
        for i in accounts:
            for j in range(len(i)):
                a.append(i)
                su.append(sum(i))
        return max(su)