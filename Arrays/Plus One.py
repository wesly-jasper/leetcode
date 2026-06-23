class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c=""
        ar=[]
        for i in range(len(digits)):
            c+=str(digits[i])
        d=int(c)
        d=d+1
        d=str(d)
        for i in d:
            ar.append(int(i))
        return ar

