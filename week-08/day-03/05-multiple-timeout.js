'use strict';

// Write a program that prints the following fruits:
// apple -> immediately
// pear -> after 1 seconds
// melon -> after 3 seconds
// grapes -> after 5 seconds

let fruits = ['apple', 'pear', 'melon', 'grapes'];
let time = [0, 1000, 3000, 5000];

console.log('apple')

setTimeout(function(fruit, time) {
    console.log('pear');
}, time);

setTimeout('pear', 1000);
setTimeout('melon', 3000);
setTimeout('grapes', 5000);
