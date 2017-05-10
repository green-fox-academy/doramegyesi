'use strict';

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

var lookForE = fruits.map(function(x) {
    var es = []
    return x.split('').join('') === x;
    if (x === 'e') {
        es.push(x);
    }
    return es;
})

console.log(lookForE);




// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.
