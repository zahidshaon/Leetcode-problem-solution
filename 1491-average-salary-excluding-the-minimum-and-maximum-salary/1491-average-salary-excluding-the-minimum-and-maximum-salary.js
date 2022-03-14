/**
 * @param {number[]} salary
 * @return {number}
 */
var average = function(salary) {
    var min= salary[0];
    var max= salary[0];
    var sum=0;
    for(let i=0;i<salary.length;i++){
        if(salary[i]<=min){
            min=salary[i];
        }
        if(salary[i]>=max){
            max=salary[i];
        }
    }
    for(let i=0;i<salary.length;i++){
         sum=sum+salary[i];
    }
    return (sum-(min+max))/(salary.length-2);    
};