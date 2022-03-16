/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function(n) {
    var product=1;
    var sum=0;
    var c=0;
    var a=[];
    while(n>0){
        a[c]=parseInt(n%10);
        n=parseInt(n/10);
        c++;
    }
    console.log(a)
    for(let i=0;i<a.length;i++){
        product=product*a[i];
        sum=sum+a[i];
    }
    return (product-sum);
};