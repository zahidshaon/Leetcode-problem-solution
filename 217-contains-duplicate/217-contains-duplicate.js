/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    var b = [];
    for(var i=0; i<nums.length; i++){
        b[i]=nums[i];
        if(i!=0){
            for(var j=0; j<b.length-1; j++){
                if(b[j]==nums[i]){
                    return true;
                }
            }
        }
    }
    return false;
}
    