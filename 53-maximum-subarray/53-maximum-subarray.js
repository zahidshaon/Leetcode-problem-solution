/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    var sum= nums[0];
    var max= nums[0];
    for(var i=1; i<nums.length; i++){
        if(sum+nums[i]>nums[i]){
            sum=sum+nums[i];
        }
        else{
            sum=nums[i];
        }
        if(max>sum){
            max=max;
        }
        else{
            max=sum;
        }
        
    }
    return max;
};