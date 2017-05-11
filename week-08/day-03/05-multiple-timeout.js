'use strict';

// Write a program that prints the following fruits:
// apple -> immediately
// pear -> after 1 seconds
// melon -> after 3 seconds
// grapes -> after 5 seconds

console.log('apple');

function printTheFruits(fruit, time) {
    setTimeout(function() {
        console.log(fruit);
    }, time)
};

printTheFruits('pear', 1000);
printTheFruits('melon', 3000);
printTheFruits('grapes', 5000);
