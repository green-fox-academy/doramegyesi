'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial


function factorio(num) {
    var total = 1;
    for (var n = 1; n <= num; n++) {
        total *= n;
    }
    return total;
}

console.log(factorio(3))
console.log(factorio(8))
console.log(factorio(21))
