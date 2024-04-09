class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeToEat(s: int) -> int:
            eatingTime = 0
            for i in piles:
                eatingTime += ceil(i/s)
            
            return eatingTime

        if len(piles) == 1:
            return ceil(piles[0]/h)
        
        l,r = 1, max(piles)

        sol = r

        while l<=r:
            mid = (r+l)//2
            eatTime = timeToEat(mid)
            if  eatTime <= h:
                sol = min(sol, mid)
                r = mid - 1
            elif eatTime > h:
                l = mid + 1

        return sol

        