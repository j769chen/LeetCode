class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #First, create a list of tuples containing position and speed, sorted (i.e. first by position, 
        # then ties broken by speed). Then create a list of each car's time to destination based on 
        # values in the list of tuples (timeToDest.append((target-t[0])/t[1])). Finally, iterate 
        # through the time to destination list in reverse order, and if the current time is greater than 
        # the current slowest time, that is one more car fleet.
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