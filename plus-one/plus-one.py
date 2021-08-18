class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for number in range(len(digits)-1,-1,-1):
            if(digits[number]<9):
                digits[number]+=1
                return digits
            digits[number]=0
        
        return [1] + digits