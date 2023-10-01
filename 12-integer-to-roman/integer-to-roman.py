class Solution:
    def intToRoman(self, num: int) -> str:
        solString = ""
    # largestToCheck = 1000
    # if largestToCheck ==
        if num >= 1000:
            temp = num//1000
            for i in range(temp):
                    solString += "M"
            num = num - (temp*1000)
        
        if num >= 900:
            solString += "CM"
            num = num - 900
        
        if num >= 500:
            solString += "D"
            num = num - 500
        
        if num >= 400:
            solString += "CD"
            num = num - 400
        
        if num >= 100:
            temp = num//100
            for i in range(temp):
                solString += "C"
            num = num - (temp*100)
        
        if num >= 90:
            solString += "XC"
            num = num - 90
            
        if num >= 50:
            solString += "L"
            num = num - 50
            
        if num >= 40:
            solString += "XL"
            num = num - 40
        
        if num >= 10:
            temp = num//10
            for i in range(temp):
                solString += "X"
            num = num - (temp*10)
        
        if num >= 9:
            solString += "IX"
            num = num - 9
        
        if num >= 5:
            solString += "V"
            num = num - 5
            
        if num >= 4:
            solString += "IV"
            num = num - 4
        
        if num >= 1:
            for i in range(num):
                solString += "I"

        return solString