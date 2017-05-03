'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

function sum(num) {
    var total = 0;
    for (var n = 0; n <= num; n++) {
        total += n;
    }
    return total;
}

console.log(sum(3));
console.log(sum(8));
console.log(sum(21));
