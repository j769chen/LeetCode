class Solution:
    def hammingWeight(self, n: int) -> int:
        bitString = bin(n)[2:]
        
        count = 0
        
        for b in bitString:
            if b == '1':
                count += 1
        
        return count