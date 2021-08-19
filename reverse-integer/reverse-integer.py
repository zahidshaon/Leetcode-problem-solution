class Solution:
    def reverse(self, x: int) -> int:
        reverse=0
        sign=-1 if x<0 else 1
        x *= sign
        while x:
            reverse=(reverse*10)+(x%10)
            x//=10
            
        return 0 if (reverse < -2**31 or reverse > 2**31 - 1) else reverse*sign
            
      
        