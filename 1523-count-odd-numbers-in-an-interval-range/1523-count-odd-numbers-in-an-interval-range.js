/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countOdds = function(low, high) {
    var c = 0;
    if(low==high & low%2==1){
      return 1;
    }
    for(let i= low; i<high+1; i++){
        if(low==high){
            break;
        }
        else if(i%2==1){
            c++;
        }
    }
    return c;
    
};