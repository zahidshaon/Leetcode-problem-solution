/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
    var c=[];
    var x=0;
    for(var i=0;i<nums1.length;i++){                            
        for(var j=0;j<nums2.length;j++){                          
            if(nums1[i]==nums2[j]){                                  
                c[x]=nums1[i];
                nums2[j]=null;
                x++;
                break;
            }
        };
    };
    return c;
};