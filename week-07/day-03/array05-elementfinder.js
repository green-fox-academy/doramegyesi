'use strict';

// Check if the array contains "7" if it contains print "Hoorray" otherwise print "Noooooo"

var numbers = [1,2,3,4,5,6,8];
function sevenChecker(input) {
    if (input.indexOf(7) >= 0) {
        console.log('Hoorray');
    } else {
        console.log('Noooooo');
    }
}

sevenChecker(numbers);
