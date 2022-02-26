/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    var x=m;
    for(var i=0;i<n;i++){                                            //O(n)
        if(nums1[x] == 0 || nums1[x] == null){
            nums1[x]=nums2[i];
            x++;
        }
    };
    for(var j=0;j<nums1.length;j++){                                //O(n)
        for(var k=j+1;k<nums1.length;k++){                          //O(n)
            if(nums1[k]<nums1[j]){                                  //O(n)
                temp=nums1[j];
                nums1[j]=nums1[k];
                nums1[k]=temp;
            }
        };
    };
    return nums1;        
};
                                                                    //total= O(n + (n*n*n)) = O(n + n^3) = O(n^3) 