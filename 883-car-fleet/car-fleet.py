class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carMap = sorted(zip(position, speed))
        timeToDest = []

        for t in carMap:
            timeToDest.append((target-t[0])/t[1])
        
        currMax = 0
        count = 0

        for t in reversed(timeToDest):
            if t > currMax:
                currMax = t
                count += 1
        
        return count