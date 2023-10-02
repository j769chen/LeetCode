class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        solString = ""
    # largestToCheck = 1000
    # if largestToCheck ==
        solString = ""
        numsToCheck = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    
        for i in numsToCheck:
            if num >= i:
                if i == 1000 or i == 100 or i == 10:
                    temp = num//i
                    for j in range(temp):
                        solString += dict[i]
                    num -= temp * i
                elif i == 1:
                    for j in range(num):
                        solString += dict[i]
                else:
                    solString += dict[i]
                    num -= i
        return solString