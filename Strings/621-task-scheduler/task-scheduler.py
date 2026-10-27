from collections import Counter
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq=Counter(tasks).values()
        maxf=max(freq)
        c=sum(f==maxf for f in freq)
        return max(len(tasks),(maxf-1)*(n+1)+c)