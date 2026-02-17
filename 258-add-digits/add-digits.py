class Solution:
    def addDigits(self, num: int) -> int:
        
        while num >= 10:          # more than 1 digit
            s = 0
            
            while num > 0:
                s += num % 10
                num //= 10
                
            num = s               # repeat on new sum
            
        return num
