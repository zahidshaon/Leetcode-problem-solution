class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=-inf
        sum=0
        for number in nums:
            sum=sum+number
            res=max(res,sum)
            sum=max(sum,0)
        
        return res
        