class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0):
            return False
        elif(x==0 or x<10):
            return True
        reverse=0
        y=x
        while x:
            reverse=reverse*10 + x%10
            x//=10
        
        if (reverse==y):
            return reverse
            