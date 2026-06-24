class Solution:
    def reverseWords(self, s: str) -> str:
        b=""
        a=list(map(str,s.split()))
        for i in range(len(a)-1,-1,-1):
            b+=a[i]
            b+=" "
        return b.rstrip()