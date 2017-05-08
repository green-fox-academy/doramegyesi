'use strict';
var test = require('tape');

// length should be 10
// [0,0,0,4,5,6,7,8,9] => ok
// [9,0,0,4,5,6,7,8,9] => Should fail
// [1,2,3,4,5,6,7,8,9] => ok
// [2,1,3,4,5,6,7,8,9] => ok
// [9,8,7,6,5,1,2,4,9] => Should fail
// [9,8,7,6,5,1,2,4,'u'] => Shold fail (non integer)

var sline = [0,1,21,2,3,4];
var correct = [1,2,3,4,5,6,7,8,9];
var incomplete = [0,0,3,4,5,6,7,8,9];
var invalid = ['0',2,3,4,5,6,7,8,9];
var short = [4,5,6,7,8,9];

function validator() {
    return false;
}

test('data structure test', function (t) {
    t.equals(validator(sline, 10));
    t.end();
})
