/*Write a function, that takes a string as an argument and returns a dictionary with all letters in the string as keys, and numbers as values that shows how many occurrences there are.
Create a test for that.*/

'use strict';

function countLetters(w) {
    var letters = w.split('');
    var dict = {};
    letters.forEach(function (l) {
        if (l in dict) {
            dict[l] += 1;
        } else {
            dict[l] = 1;
        }
    });
    return dict;
}

module.exports = countLetters;

console.log(countLetters('cockroach'))
