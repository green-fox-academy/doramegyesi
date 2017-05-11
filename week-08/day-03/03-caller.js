'use strict';

// Implement the selectLastEvenNumber function that takes an array and callback,
// it should call the callback immediately with the last even number on the array


function printNumber(num) {
  console.log(num);
};

function selectLastEvenNumber(array, callback) {
    var evenNumbers = [];
    array.filter(function (e) {
        if (e % 2 === 0) {
            evenNumbers.push(e);
        }
        callback(evenNumbers[evenNumbers.length - 1])
    })
};

selectLastEvenNumber([2, 5, 7, 8, 9, 11], printNumber); // should print 8
